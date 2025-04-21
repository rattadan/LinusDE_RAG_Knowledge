import { AgentRuntime } from "../../packages/core/src/runtime";
import type { Memory } from "../../packages/core/src/types";
import type { Tweet } from "agent-twitter-client";

interface TwitterMemory extends Memory {
    content: {
        text: string;
        mentions: Array<{
            username: string;
            userId: string;
            startIndex: number;
            endIndex: number;
        }>;
    };
    metadata: {
        tweetId: string;
        conversationId: string;
        isRetweet: boolean;
        isQuote: boolean;
        timestamp: number;
    };
}
import { promises as fs } from "fs";
import { join } from "path";

interface KnowledgeCategory {
    name: string;
    keywords: string[];
    file: string;
}

const KNOWLEDGE_CATEGORIES: KnowledgeCategory[] = [
    {
        name: "Blockchain Technology",
        keywords: ["blockchain", "crypto", "consensus", "smart contracts", "defi", "layer2"],
        file: "01_blockchain_technology.md"
    },
    {
        name: "Urban Mobility",
        keywords: ["transportation", "mobility", "transit", "traffic", "cities"],
        file: "02_urban_mobility.md"
    },
    // Add other categories...
];

export class TweetKnowledgeProcessor {
    private knowledgeDir: string;

    constructor(private runtime: AgentRuntime) {
        this.knowledgeDir = join(__dirname, "linus-knowledge");
    }

    async processTweetMemories(tweets: TwitterMemory[], limit: number = 100) {
        const categorizedTweets = this.categorizeTweets(tweets.slice(0, limit));
        await this.updateKnowledgeFiles(categorizedTweets);
    }

    private categorizeTweets(tweets: TwitterMemory[]) {
        const categorized = new Map<string, TwitterMemory[]>();
        
        for (const tweet of tweets) {
            const category = this.classifyTweet(tweet);
            if (category) {
                if (!categorized.has(category.name)) {
                    categorized.set(category.name, []);
                }
                categorized.get(category.name)?.push(tweet);
            }
        }

        return categorized;
    }

    private classifyTweet(tweet: TwitterMemory): KnowledgeCategory | null {
        const content = tweet.content.text.toLowerCase();
        
        for (const category of KNOWLEDGE_CATEGORIES) {
            if (category.keywords.some(keyword => content.includes(keyword.toLowerCase()))) {
                return category;
            }
        }

        return null;
    }

    private async updateKnowledgeFiles(categorizedTweets: Map<string, TwitterMemory[]>) {
        for (const [categoryName, tweets] of categorizedTweets) {
            const category = KNOWLEDGE_CATEGORIES.find(c => c.name === categoryName);
            if (!category) continue;

            const filePath = join(this.knowledgeDir, category.file);
            await this.updateKnowledgeFile(filePath, tweets);
        }
    }

    private async updateKnowledgeFile(filePath: string, tweets: TwitterMemory[]) {
        try {
            // Read existing content
            let content = await fs.readFile(filePath, 'utf8');
            
            // Add new section for tweet insights
            const tweetInsights = this.formatTweetInsights(tweets);
            content += "\n\n## Recent Insights from Social Media\n" + tweetInsights;

            // Write updated content
            await fs.writeFile(filePath, content, 'utf8');
        } catch (error) {
            console.error(`Error updating knowledge file ${filePath}:`, error);
        }
    }

    private formatTweetInsights(tweets: TwitterMemory[]): string {
        return tweets
            .map(tweet => {
                const date = new Date(tweet.metadata.timestamp).toISOString().split('T')[0];
                return `### Insight (${date})\n${tweet.content}\n`;
            })
            .join("\n");
    }

    // Schedule routine to run periodically
    async scheduleRoutine(intervalHours: number = 24) {
        setInterval(async () => {
            // Get tweets from the Twitter memory manager
            const twitterMemoryManager = this.runtime.getMemoryManager('twitter');
            if (!twitterMemoryManager) {
                console.error('Twitter memory manager not found');
                return;
            }
            const memories = await twitterMemoryManager.getMemories({
                roomId: this.runtime.agentId,
                count: 100,
                unique: true
            });
            const recentTweets = memories as TwitterMemory[];
            await this.processTweetMemories(recentTweets);
        }, intervalHours * 60 * 60 * 1000);
    }
}
