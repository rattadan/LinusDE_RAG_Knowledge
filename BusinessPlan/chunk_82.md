## Chunk 82

**Original Text:**

Service interruption and price of Google APIs: nRide
relies on google APIs for serving maps, geolocation, and
calculating routes. An interruption in these services would
result in the app being unusable. There is also a risk that
nRide will face high service costs for using these APIs,
thereby eroding profits

If we start seeing issues with google, there are other
alternatives out there like Open Street Maps which we can
explore. Battery life: nRide is heavy on networking which puts strain
on the device’s battery (cellular or wifi). This is a factor that
could undermine the user-experience

There are low hanging fruits we can implement such as a
better encoding scheme, and more advanced retry logic to
reduce this risk if it becomes an issue

NFC handshake:The only part in the roadmap where we are
still not sure that a solution is feasible is the one concerning
the NFC handshake whereby users exchange secrets to
unlock escrow funds by tapping phones.

---

**LLM Contextual Output:**

It seems like you're discussing potential risks and challenges with the nRide app, specifically related to Google APIs, battery life, and alternative solutions.

Here are some specific points raised:

1. **Google API interruption**: The app relies on Google services for map rendering, geolocation, and route calculation. An interruption in these services would indeed make the app unusable.
2. **High service costs**: The risk of high service costs associated with using Google APIs could negatively impact profits.
3. **Battery life concerns**: Battery life is a significant issue due to the app's heavy networking requirements through cellular or Wi-Fi connections.
4. **Low-hanging fruits**: Implementing better encoding schemes and more advanced retry logic can help mitigate these risks, reducing the likelihood of app instability.

Regarding NFC (Near Field Communication) handshake, it's an interesting aspect that requires further exploration:

1. **Infeasibility**: You're unsure whether a solution is feasible for this specific use case. This may be due to technical or practical challenges.
2. **Alternative solutions**: There might be alternative methods that could achieve similar results without the NFC handshake.

Some potential questions to consider as you move forward:

* What are the primary concerns driving the need for an NFC handshake in nRide?
* Are there any specific use cases where the NFC handshake is particularly critical or necessary?
* Are there other alternatives or solutions that could address these concerns without resorting to NFC?
