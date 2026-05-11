from sentence_transformers import util

from embedder import model


def aggregate_chunks(retrieved_chunks):

    aggregated_context = []

    used = set()

    embeddings = model.encode(retrieved_chunks)

    for i in range(len(retrieved_chunks)):

        if i in used:
            continue

        current_group = [retrieved_chunks[i]]

        used.add(i)

        for j in range(i + 1, len(retrieved_chunks)):

            if j in used:
                continue

            similarity = util.cos_sim(
                embeddings[i],
                embeddings[j]
            ).item()

            if similarity > 0.7:

                current_group.append(
                    retrieved_chunks[j]
                )

                used.add(j)

        merged_chunk = "\n\n".join(current_group)

        aggregated_context.append(merged_chunk)

    return aggregated_context