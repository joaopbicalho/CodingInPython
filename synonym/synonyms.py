import math

def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    vecs_dot = 0
    vecs_dot = sum(vec1[key]*vec2.get(key, 0) for key in vec1)
    if vecs_dot == 0:
        return -1
    mag_vec1 = 0
    for key in vec1:
        mag_vec1 += (vec1[key] * vec1[key])
    mag_vec2 = 0
    for key in vec2:
        mag_vec2 += (vec2[key] * vec2[key])
    mags = math.sqrt((mag_vec1 * mag_vec2))
    sim = vecs_dot/mags
    return sim


def build_semantic_descriptors(sentences):
    d = {}
    for sentence in range(len(sentences)):
        for word in range(len(sentences[sentence])):
            for i in range(len(sentences[sentence])):
                if sentences[sentence][word] == sentences[sentence][i] and i != word:
                    sentences[sentence][i] = -1
        for word in range(len(sentences[sentence])):
            if sentences[sentence][word] not in d.keys() and sentences[sentence][word] != -1:
                d[sentences[sentence][word]] = {}
            for i in range(len(sentences[sentence])):
                if i != word and sentences[sentence][i] != -1 and sentences[sentence][word] != -1:
                    if sentences[sentence][i] not in d[sentences[sentence][word]].keys():
                        d[(sentences[sentence][word])][sentences[sentence][i]] = 1
                    else:
                        d[(sentences[sentence][word])][sentences[sentence][i]] += 1
    return d



def build_semantic_descriptors_from_files(filenames):
    files = []
    text = ""
    for i in range(len(filenames)):
        text += open(filenames[i], "r", encoding="latin1").read()
    text = text.replace(".", "?").replace("!", "?")
    text = text.replace(",", ";").replace("-", ";").replace("--", ";").replace(":", ";")
    text = text.replace(";", " ")
    text = text.lower()
    text = text.split("?")
    for i in range(len(text)):
        text[i] = text[i].split()
    return build_semantic_descriptors(text)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    x = []
    if word in semantic_descriptors:
        word_v = semantic_descriptors[word]
    else:
        word_v = {1:-1}
    for i in range(len(choices)):
        if choices[i] in semantic_descriptors:
            choices_v = semantic_descriptors[choices[i]]
            x.append(similarity_fn(word_v, choices_v))
        else:
            x.append(-1)
    best_choice_val = max(x)
    best_choice = choices[x.index(best_choice_val)]
    return best_choice


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    right = 0
    text = open(filename, "r", encoding="latin-1").read()
    text = text.split("\n")
    for i in range(len(text)):
        text[i] = text[i].split(" ")
        word = text[i][0]
        correct_choice = text[i][1]
        choices = text[i][2:]
        AI = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
        if AI == correct_choice:
            right += 1
    return ((right/(len(text)))*100)

if __name__ == '__main__':
    #x = run_similarity_test("test.txt", descriptors, cosine_similarity)
    filenames = ["wp.txt", "sw.txt"]
    y = build_semantic_descriptors_from_files(filenames)
    z = run_similarity_test("test.txt", y, cosine_similarity)
    #L = [["i","i","am", "a", "sick", "man"],["i", "am", "a", "spiteful", "man"],["i", "am", "an", "unattractive", "man"],["i", "believe", "my" ,"liver", "liver" ,"diseased", "is", "diseased"],["however", "i", "know", "nothing", "at", "all", "about", "my","disease","disease","and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
    #x = build_semantic_descriptors(L)




