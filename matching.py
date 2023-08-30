from scipy import spatial


#cosine similarity measures
def matching(A, B):
    #score = 1 - spatial.distance.cosine(img1,img2)
    #score_eu = 1 - spatial.distance.euclidean(A, B)
    score_city = 1 - spatial.distance.cityblock(A, B)
    #if score_eu > 0.70 or score_city > 0.70:
    return score_city
    #else:
     #   print("not matched")
