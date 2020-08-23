from nltk.corpus import wordnet
import logging

list_of_words = ["food", "travel", "housing", "leisure", "clothing"]
def process_transaction_response(response : dict):
    transactions = response["transactions"]
    logging.basicConfig(filename="wordSimilarity.log", filemode="w+", format="%(levelname)s %(message)s", level=logging.INFO)
    for i, transaction in enumerate(transactions):
        words_values = {"N/A": 0} ## default to N/A
        category = transaction["category"]
        word1 = wordnet.synsets(category[0])
        for ourCategory in list_of_words:
            word2 = wordnet.synsets(ourCategory)
            
            if word1 and word2:
                s = word1[0].wup_similarity(word2[0])
                words_values[ourCategory] = s
                logging.info("%s and %s compare: \n \t Score: %.2f \n" % (word1[0], word2[0], s))
            else:
                logging.info("Skipping", ourCategory, "... \n")
        max_key = max(words_values, key=words_values.get)
        response["transactions"][i]["ourCategory"] = max_key

    print(response)
    ## only compare first category


