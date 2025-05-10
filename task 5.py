from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("\n--- Sentiment Analysis Result ---")
    print(f"Sentence: {sentence}")
    print(f"Negative: {sentiment_dict['neg'] * 100:.2f}%")
    print(f"Neutral : {sentiment_dict['neu'] * 100:.2f}%")
    print(f"Positive: {sentiment_dict['pos'] * 100:.2f}%")

    # Determine overall sentiment
    compound = sentiment_dict['compound']
    if compound >= 0.05:
        overall = "Positive"
    elif compound <= -0.05:
        overall = "Negative"
    else:
        overall = "Neutral"

    print(f"Overall Sentiment: {overall}")

def main():
    analyzer = SentimentIntensityAnalyzer()
    print("Sentiment Analysis Tool (type 'exit' to quit)\n")

    count = 1
    while True:
        sentence = input(f"Enter sentence {count}: ").strip()
        if sentence.lower() == 'exit':
            print("\nExiting Sentiment Analysis Tool. Goodbye!")
            break
        elif sentence == "":
            print("⚠️  Please enter a non-empty sentence.\n")
            continue

        sentiment_scores(sentence)
        count += 1

if __name__ == "__main__":
    main()
