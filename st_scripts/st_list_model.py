import flatten_dict
import git
import pandas as pd
import streamlit as st

from st_scripts.st_utils import MODELS_PARAMETERS, MODELS_EVALUATION_METRICS, MODELS_COMMITS


def get_model_info(model_commit: git.Commit) -> dict:
    model_commit_info = {
        "hash": model_commit.hexsha,
        "message": model_commit.message,
        "committed_datetime": str(model_commit.committed_datetime),
        "committer": str(model_commit.committer),
    }

    return {
        "commit": model_commit_info,
        **MODELS_PARAMETERS[model_commit.hexsha],
        "evaluation": MODELS_EVALUATION_METRICS[model_commit.hexsha],
    }


MODELS_DF = (
    pd.DataFrame([
        flatten_dict.flatten(get_model_info(model_commit), reducer="dot")
        for model_commit in MODELS_COMMITS
    ])
    .sort_values("commit.committed_datetime").reset_index(drop=True)
    .sort_values("commit.committed_datetime", ascending=False)
)

def st_list_model():
    st.markdown("### Models list")

    columns = st.beta_columns(5)

    columns[0].text("Show columns for")
    commit_column = columns[1].checkbox("commits", value=True)
    model_column = columns[2].checkbox("model parameters", value=True)
    train_column = columns[3].checkbox("train parameters", value=True)
    eval_column = columns[4].checkbox("evaluation metrics", value=True)

    def show_column(column: str) -> bool:
        return {
            (commit_column or not column.startswith("commit."))
            and (model_column or not column.startswith("model."))
            and (train_column or not column.startswith("train."))
            and (eval_column or not column.startswith("evaluation."))
        }
    
    st.table(MODELS_DF.filter(items=[column for column in MODELS_DF if show_column(column)]))