# MathMetric

MathMetric is a Tkinter-based desktop app that bundles multiple math utilities:
- Area and volume calculators
- GCD/LCM tool
- Unit conversion
- Graph plotting
- Quiz mode

## Professionalized Repository Layout

```
MathMetric/
├── StudyProjectfinal.py     # Main GUI application entry point
├── unitcalc.py              # Unit conversion definitions
├── tkin.py                  # Standalone unit converter prototype
├── assets/
│   └── images/              # UI image assets
├── data/
│   └── quiz.json            # Quiz question dataset
├── .gitignore
└── README.md
```

## Run

```bash
python StudyProjectfinal.py
```

## Notes

- The app now resolves assets and data through explicit folder paths (`assets/images` and `data`) for cleaner project organization and easier scaling.
- Keep new images in `assets/images/` and structured datasets in `data/`.
