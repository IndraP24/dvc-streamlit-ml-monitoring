from PIL import Image
# Warning: this is private internal dvc api, it may change for future dvc versions
from dvc.repo.get import get
import numpy as np
import pandas as pd
import streamlit as st
import tensorflow as tf

from scripts.params import TRAIN_DIR, IMG_SIZE
from st_scripts.st_utils import REPO, ROOT_DIR, get_model_backbone, st_model_multiselect