import numpy as np


def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / np.sum(exp_x)


def print_matrix(title, matrix, row_labels=None, col_labels=None):
    print()
    print(title)
    print("=" * len(title))

    if col_labels:
        print(" " * 12, end="")
        for label in col_labels:
            print(f"{label:>12}", end="")
        print()

    for i, row in enumerate(matrix):
        if row_labels:
            print(f"{row_labels[i]:>10}  ", end="")
        for value in row:
            print(f"{value:>12.4f}", end="")
        print()


def main():
    tokens = ["I", "love", "AI"]

    embeddings = np.array([
        [1.0, 0.0, 0.0, 0.2],
        [0.8, 0.7, 0.0, 0.1],
        [0.0, 0.9, 1.0, 0.3],
    ])

    W_q = np.array([
        [0.8, 0.1, 0.0],
        [0.2, 0.9, 0.1],
        [0.0, 0.3, 0.8],
        [0.1, 0.0, 0.5],
    ])

    W_k = np.array([
        [0.7, 0.2, 0.1],
        [0.1, 0.8, 0.2],
        [0.0, 0.2, 0.9],
        [0.2, 0.1, 0.4],
    ])

    W_v = np.array([
        [1.0, 0.0, 0.2],
        [0.0, 1.0, 0.1],
        [0.1, 0.2, 1.0],
        [0.3, 0.1, 0.4],
    ])

    print("Transformer Attention Demo")
    print("=" * 50)
    print("Tokens:", tokens)
    print("Embedding shape:", embeddings.shape)

    Q = embeddings @ W_q
    K = embeddings @ W_k
    V = embeddings @ W_v

    print_matrix("Query Matrix Q", Q, tokens)
    print_matrix("Key Matrix K", K, tokens)
    print_matrix("Value Matrix V", V, tokens)

    d_k = K.shape[1]
    scores = Q @ K.T / np.sqrt(d_k)

    print_matrix(
        "Attention Scores",
        scores,
        row_labels=tokens,
        col_labels=tokens,
    )

    attention_weights = np.array([
        softmax(row) for row in scores
    ])

    print_matrix(
        "Attention Weights",
        attention_weights,
        row_labels=tokens,
        col_labels=tokens,
    )

    output = attention_weights @ V

    print_matrix("Attention Output", output, tokens)

    print()
    print("Interpretation")
    print("=" * 50)

    for i, token in enumerate(tokens):
        most_attended_index = np.argmax(attention_weights[i])
        most_attended_token = tokens[most_attended_index]
        weight = attention_weights[i][most_attended_index]

        print(
            f"Token '{token}' pays most attention to "
            f"'{most_attended_token}' with weight {weight:.4f}"
        )

    print()
    print("Summary")
    print("=" * 50)
    print("Query means: what this token is looking for.")
    print("Key means: what each token can match with.")
    print("Value means: the information each token provides.")
    print("Attention weights decide how much information to take from each token.")
    print("Self-attention mixes token information based on relevance.")


if __name__ == "__main__":
    main()