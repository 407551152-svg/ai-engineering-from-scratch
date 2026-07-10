import math


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def magnitude(v):
    return math.sqrt(sum(x * x for x in v))


def cosine_similarity(a, b):
    return dot(a, b) / (magnitude(a) * magnitude(b))


query = [1.0, 0.8, 0.1]

documents = {
    "文档A：介绍 AI 工程": [0.9, 0.7, 0.2],
    "文档B：介绍做饭技巧": [0.1, 0.2, 0.9],
    "文档C：介绍机器学习": [0.95, 0.85, 0.1],
}

print("查询向量:", query)
print()

best_doc = None
best_score = -1

for title, vector in documents.items():
    score = cosine_similarity(query, vector)
    print(title, "相似度:", round(score, 4))

    if score > best_score:
        best_score = score
        best_doc = title

print()
print("最相关的文档是:", best_doc)
print("最高相似度:", round(best_score, 4))