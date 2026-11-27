# DocMeta-ID

Experimental framework for OCR-free metadata extraction
from Indonesian official documents.

## Research Objective

This project investigates the effect of different
visual encoder architectures on document metadata
extraction using a Donut-inspired architecture.

## Target Metadata

- Document numbers
- Document subject / perihal / tentang

## Model Configurations

| Model | Visual Encoder | Decoder |
|---|---|---|
| Donut-Swin | Swin Transformer | BART |
| Donut-SigLIP | SigLIP Vision Encoder | BART |
| Donut-ResNet50 | ResNet50 | BART |

## Dataset

The project uses the DocMeta-ID dataset.

Dataset access and redistribution follow the
permissions and terms documented in its dataset card.

## Repository Structure

- `configs/`: experiment configurations
- `docs/`: research documentation
- `schemas/`: data validation schemas
- `src/`: project implementation
- `scripts/`: executable utilities
- `tests/`: automated tests
- `notebooks/`: exploratory notebooks

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Reproducibility

Every experiment should record:

- Dataset revision
- Code commit
- Model checkpoint
- Random seed
- Training configuration
- Evaluation metrics

## Status

Research prototype. Training and evaluation
configurations are subject to change.

## License

The source code is distributed under the MIT License.
Third-party components retain their original licenses.
