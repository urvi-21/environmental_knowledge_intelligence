import streamlit as st

from scraper import extract_webpage_text
from preprocess import clean_text
from chunker import chunk_text
from embedder import create_embeddings
from retriever import VectorStore, retrieve_chunks
from aggregator import aggregate_chunks
from generator import generate_response
from extractor import extract_environmental_information
from insight_extractor import generate_research_insights
from confidence import calculate_confidence
from trend_analysis import extract_environmental_trends
from cross_source_analysis import (
    generate_cross_source_insights
)


# ----------------------------------------
# PAGE CONFIG
# ----------------------------------------

st.set_page_config(
    page_title="Environmental Knowledge Intelligence Framework",
    page_icon="🌍",
    layout="wide"
)


# ----------------------------------------
# SESSION STATE INITIALIZATION
# ----------------------------------------

if "processed" not in st.session_state:
    st.session_state.processed = False

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "summary" not in st.session_state:
    st.session_state.summary = None

if "extracted_information" not in st.session_state:
    st.session_state.extracted_information = None

if "chunk_count" not in st.session_state:
    st.session_state.chunk_count = 0

if "source_mapping" not in st.session_state:
    st.session_state.source_mapping = None


# ----------------------------------------
# SIDEBAR
# ----------------------------------------

with st.sidebar:

    st.header("Framework Pipeline")

    st.markdown(
        """
        1. Multi-Source Web Extraction  
        2. Semantic Chunking  
        3. Embedding Generation  
        4. Vector Retrieval  
        5. Environmental Re-Ranking  
        6. Context Aggregation  
        7. Grounded Scientific Synthesis  
        """
    )

    st.header("Framework Highlights")

    st.markdown(
        """
        - Attention-Inspired Retrieval  
        - Environmental Importance Scoring  
        - Scientific Density Prioritization  
        - Context Aggregation Layer  
        - Cross-Source Evidence Synthesis  
        - Explainable Retrieval Pipeline  
        """
    )

    st.header("Recommended URLs")

    st.markdown(
        """
        https://climate.nasa.gov/causes/

        https://climate.nasa.gov/effects/

        https://climate.nasa.gov/vital-signs/sea-level/
        """
    )


# ----------------------------------------
# TITLE
# ----------------------------------------

st.title(
    "Attention-Inspired Environmental Knowledge Intelligence Framework for Grounded Decision Support"
)

st.markdown(
    """
    Lightweight Retrieval-Augmented Framework for
    Environmental Web Information Extraction,
    Cross-Source Scientific Synthesis,
    Summarisation, and Grounded Q&A
    """
)


# ----------------------------------------
# MULTI-URL INPUT
# ----------------------------------------

urls_input = st.text_area(
    "Enter up to 3 Environmental Webpage URLs (one per line)"
)


# ----------------------------------------
# PROCESS BUTTON
# ----------------------------------------

if st.button("Process Sources"):

    urls = [
        url.strip()
        for url in urls_input.split("\n")
        if url.strip()
    ]

    if len(urls) == 0:

        st.warning(
            "Please enter at least one valid URL."
        )

        st.stop()

    if len(urls) > 3:

        st.warning(
            "Maximum 3 URLs allowed."
        )

        st.stop()

    try:

        # ----------------------------------------
        # MULTI-SOURCE EXTRACTION
        # ----------------------------------------

        all_chunks = []

        source_mapping = []

        for source_url in urls:

            with st.spinner(
                f"Processing source: {source_url}"
            ):

                raw_text = extract_webpage_text(
                    source_url
                )

                cleaned_text = clean_text(
                    raw_text
                )

                if len(cleaned_text.split()) < 50:
                    continue

                chunks = chunk_text(
                    cleaned_text,
                    chunk_size=80,
                    overlap=20
                )

                for chunk in chunks:

                    all_chunks.append(chunk)

                    source_mapping.append(
                        source_url
                    )

        # ----------------------------------------
        # VALIDATION
        # ----------------------------------------

        if len(all_chunks) == 0:

            st.error(
                """
                No meaningful content could be extracted.

                Possible reasons:
                - websites blocked scraping
                - dynamic rendering
                - Cloudflare protection
                """
            )

            st.stop()

        st.success(
            "Sources processed successfully."
        )

        # ----------------------------------------
        # EMBEDDINGS
        # ----------------------------------------

        with st.spinner(
            "Generating embeddings..."
        ):

            embeddings = create_embeddings(
                all_chunks
            )

            vector_store = VectorStore(
                embeddings
            )

        st.success(
            "Vector database created."
        )

        # ----------------------------------------
        # SUMMARY
        # ----------------------------------------

        summary_context = " ".join(
            all_chunks[:10]
        )

        summary_question = (
            "Provide a concise scientific summary "
            "of the environmental sources."
        )

        with st.spinner(
            "Generating environmental summary..."
        ):

            summary = generate_response(
                summary_context,
                summary_question
            )

        # ----------------------------------------
        # INFORMATION EXTRACTION
        # ----------------------------------------

        with st.spinner(
            "Extracting structured environmental information..."
        ):

            extracted_information = (
                extract_environmental_information(
                    summary_context
                )
            )

        # ----------------------------------------
        # SAVE SESSION STATE
        # ----------------------------------------

        st.session_state.processed = True

        st.session_state.chunks = all_chunks

        st.session_state.vector_store = vector_store

        st.session_state.summary = summary

        st.session_state.extracted_information = (
            extracted_information
        )

        st.session_state.chunk_count = (
            len(all_chunks)
        )

        st.session_state.source_mapping = (
            source_mapping
        )

    except Exception as e:

        st.error(
            f"An error occurred: {str(e)}"
        )


# ----------------------------------------
# DISPLAY RESULTS
# ----------------------------------------

if st.session_state.processed:

    chunks = st.session_state.chunks

    vector_store = st.session_state.vector_store

    summary = st.session_state.summary

    extracted_information = (
        st.session_state.extracted_information
    )

    source_mapping = (
        st.session_state.source_mapping
    )

    # ----------------------------------------
    # METRICS
    # ----------------------------------------

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Chunks",
        st.session_state.chunk_count
    )

    col2.metric(
        "Sources",
        len(set(source_mapping))
    )

    col3.metric(
        "Embedding Dimension",
        384
    )

    # ----------------------------------------
    # SUMMARY
    # ----------------------------------------

    st.subheader(
        "Environmental Summary"
    )

    st.write(summary)

    # ----------------------------------------
    # STRUCTURED INFORMATION
    # ----------------------------------------

    st.subheader(
        "Structured Environmental Information"
    )

    st.write(extracted_information)

    # ----------------------------------------
    # QUESTION INPUT
    # ----------------------------------------

    st.subheader(
        "Interactive Environmental Q&A"
    )

    question = st.text_input(
        "Ask Environmental Question"
    )

    # ----------------------------------------
    # QUESTION ANSWERING
    # ----------------------------------------

    if question:

        try:

            # ----------------------------------------
            # RETRIEVAL
            # ----------------------------------------

            with st.spinner(
                "Retrieving relevant environmental context..."
            ):

                retrieved_results = (
                    retrieve_chunks(
                        question,
                        vector_store,
                        chunks
                    )
                )

            st.subheader(
                "Retrieved Context"
            )

            retrieved_chunks = []

            # ----------------------------------------
            # DISPLAY RETRIEVED CHUNKS
            # ----------------------------------------

            for i, result in enumerate(
                retrieved_results
            ):

                (
                    chunk,
                    final_score,
                    env_score,
                    sci_score,
                    semantic_score
                ) = result

                retrieved_chunks.append(
                    chunk
                )

                with st.expander(
                    f"Chunk {i+1}"
                ):

                    st.write(
                        f"Final Score: "
                        f"{round(final_score, 2)}"
                    )

                    st.write(
                        f"Semantic Score: "
                        f"{semantic_score}"
                    )

                    st.write(
                        f"Environmental Score: "
                        f"{env_score}"
                    )

                    st.write(
                        f"Scientific Density Score: "
                        f"{sci_score}"
                    )

                    # ----------------------------------------
                    # SOURCE ATTRIBUTION
                    # ----------------------------------------

                    chunk_index = chunks.index(
                        chunk
                    )

                    source_url = source_mapping[
                        chunk_index
                    ]

                    st.write(
                        f"Source: {source_url}"
                    )

                    # ----------------------------------------
                    # EXPLAINABILITY
                    # ----------------------------------------

                    reasons = []

                    if env_score > 3:
                        reasons.append(
                            "High Environmental Relevance"
                        )

                    if sci_score > 3:
                        reasons.append(
                            "Scientifically Informative"
                        )

                    if semantic_score > 7:
                        reasons.append(
                            "Strong Semantic Match"
                        )

                    st.write(
                        "Selection Reason:"
                    )

                    st.write(
                        ", ".join(reasons)
                    )

                    st.write(chunk)

            # ----------------------------------------
            # CONTEXT AGGREGATION
            # ----------------------------------------

            with st.spinner(
                "Aggregating contextual evidence..."
            ):

                aggregated_chunks = (
                    aggregate_chunks(
                        retrieved_chunks
                    )
                )

            context = "\n\n".join(
                aggregated_chunks
            )

            st.subheader(
                "Aggregated Context"
            )

            for i, chunk in enumerate(
                aggregated_chunks
            ):

                with st.expander(
                    f"Aggregated Group {i+1}"
                ):

                    st.write(chunk)

            # ----------------------------------------
            # FINAL RESPONSE
            # ----------------------------------------

            with st.spinner(
                "Generating grounded scientific response..."
            ):

                response = generate_response(
                    context,
                    question
                )

            st.subheader(
                "Grounded Response"
            )

            st.write(response)

            # ----------------------------------------
            # CONFIDENCE ESTIMATION
            # ----------------------------------------

            confidence, confidence_reason = (
                calculate_confidence(
                    retrieved_results
                )
            )

            st.subheader(
                "Confidence Estimation"
            )

            st.write(
                f"Confidence Level: {confidence}"
            )

            st.write(
                f"Reason: {confidence_reason}"
            )

            # ----------------------------------------
            # TREND ANALYSIS
            # ----------------------------------------

            with st.spinner(
                "Analyzing environmental trends..."
            ):

                environmental_trends = (
                    extract_environmental_trends(
                        context
                    )
                )

            st.subheader(
                "Environmental Trend Analysis"
            )

            st.write(
                environmental_trends
            )

            # ----------------------------------------
            # RESEARCH INSIGHTS
            # ----------------------------------------

            with st.spinner(
                "Generating research insights..."
            ):

                research_insights = (
                    generate_research_insights(
                        context
                    )
                )

            st.subheader(
                "Research Insights"
            )

            st.write(
                research_insights
            )

            # ----------------------------------------
            # CROSS-SOURCE INSIGHTS
            # ----------------------------------------

            with st.spinner(
                "Generating cross-source scientific insights..."
            ):

                cross_source_insights = (
                    generate_cross_source_insights(
                        context
                    )
                )

            st.subheader(
                "Cross-Source Environmental Insights"
            )

            st.write(
                cross_source_insights
            )

        except Exception as e:

            st.error(
                f"Question answering failed: {str(e)}"
            )