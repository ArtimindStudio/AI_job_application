# Slyde Innovations Lifestyle Demo
## Visual Reference Workspace

Automated reference acquisition pipeline for the style-injection phase.

### Directory Structure

```
Slyde_Innovations_Lifestyle_Demo/
├── Ref_A_Identity/      ← Product CMF: matte poly, steel, aluminum
├── Ref_B_Lighting/      ← Environment: 45° daylight, neutral palettes
├── Ref_C_Lifestyle/     ← Lifestyle: corporate-casual, natural interaction
├── fetch_references.py  ← Automated pipeline (Unsplash + Pexels APIs)
├── reference_metadata.json ← CMF & lighting metadata output
├── SOURCING_GUIDE.md    ← Manual search queries for premium databases
└── README.md            ← This file
```

### Quick Start

1. **Get free API keys**:
   - [Unsplash Developers](https://unsplash.com/developers)
   - [Pexels API](https://www.pexels.com/api/)

2. **Set environment variables** (PowerShell):
   ```powershell
   $env:UNSPLASH_ACCESS_KEY = "your_unsplash_key"
   $env:PEXELS_API_KEY = "your_pexels_key"
   ```

3. **Install dependencies & run**:
   ```powershell
   pip install requests
   python fetch_references.py
   ```

4. **Manual sourcing**: Follow `SOURCING_GUIDE.md` for premium databases.

### Pipeline Output
- 15 images per category (45 total) from Unsplash + Pexels
- `reference_metadata.json` with CMF analysis, lighting angles, and file integrity hashes
- Ready for Google Flow / Nano Banana Tools style-injection
