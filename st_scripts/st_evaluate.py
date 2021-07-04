import json

import dvc.api
import pandas as pd
import streamlit as st

from scripts.params import EVALUATION_DIR
from st_scripts.st_utils import st_model_selectbox, MODELS_PARAMETERS, REPO