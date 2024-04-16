from __future__ import annotations  # PEP 604 backport

import torch

import logging
import warnings

from rich.console import Console
from rich.logging import RichHandler

logging.getLogger("matplotlib").setLevel(logging.WARNING)

# For NumPy's precision errors & Matplotlib with non-GUI backend
warnings.filterwarnings("once", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=UserWarning)

logging.basicConfig(
    level=20,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=Console(stderr=True), markup=True)],
    force=True,
)
logging.captureWarnings(True)
logger = logging.getLogger("alphacube")
logargs = dict(extra={"markup": True})


if torch.cuda.is_available():
    # bf16 not considered: slightly slower than fp16
    device = torch.device("cuda")
    dtype = torch.float16
elif torch.backends.mps.is_available():
    device = torch.device("mps")
    dtype = torch.float16
else:
    device = torch.device("cpu")
    dtype = torch.float32


# Set up logging level
def set_verbose(loglevel=20):
    """
    Set the verbosity level of the logger.

    Args:
        loglevel (int): Logging level (e.g., logging.INFO, logging.DEBUG) to control the verbosity.

    Returns:
        None
    """
    logger.setLevel(loglevel)


set_verbose(loglevel=30)  # default to WARNING
