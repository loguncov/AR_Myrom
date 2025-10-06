# AR_WEB_Myrom - Replit Documentation

## Overview
AR_WEB_Myrom is an Augmented Reality web application that allows users to scan QR codes and view 3D models through their device camera. Built with A-Frame and AR.js, this project contains 45 different AR scenes, each with its own QR marker and 3D model.

**Current State:** The application is fully configured and running on Replit with a Python HTTP server serving static files on port 5000.

## Recent Changes
- **October 6, 2025**: GitHub Pages automatic deployment configured
  - Added GitHub Actions workflow for automatic deployment on every commit
  - Configured automatic publishing to GitHub Pages
- **October 6, 2025**: Initial Replit setup completed
  - Created main landing page (index.html) with navigation to all 45 AR scenes
  - Configured Python HTTP server to serve static files on port 5000
  - Set up workflow for automatic server startup
  - Created project documentation and .gitignore

## Project Architecture

### Technology Stack
- **A-Frame 1.0.4**: VR/AR framework for WebXR experiences
- **AR.js**: Augmented reality library for marker-based tracking
- **GLTF Models**: 3D model format for AR objects
- **Python HTTP Server**: Simple static file server for development

### Project Structure
```
/
├── index.html              # Main landing page with scene navigation
├── common/                 # Shared resources for all scenes
│   ├── gesture-detector.js # Touch gesture detection
│   ├── gesture-handler.js  # Gesture handling (rotate, scale)
│   └── styles.css          # Common styles
├── 01/ through 45/         # Individual AR scenes
│   ├── index.html          # Marker-based AR tracking
│   ├── image-tracking.html # NFT image tracking
│   ├── obj/                # 3D models (GLTF format)
│   └── qr/                 # QR patterns and images
└── cleanup_ar_folders.py   # Utility script for maintenance
```

### Key Features
1. **45 AR Scenes**: Each scene has a unique QR marker and 3D model
2. **Marker Tracking**: Pattern-based AR using custom QR codes
3. **Image Tracking**: NFT (Natural Feature Tracking) support
4. **Gesture Controls**: Touch gestures for rotating and scaling 3D models
5. **Modular Architecture**: Shared scripts in `common/` folder prevent code duplication

## Development Setup

### Running Locally
The server runs automatically via the configured workflow:
- Server: Python HTTP server
- Port: 5000
- Host: 0.0.0.0 (allows Replit proxy access)

### Testing AR Scenes
1. Open the main page to see all available scenes
2. Click on any scene to access its AR experience
3. Allow camera access when prompted
4. Point camera at the corresponding QR code marker
5. Use touch gestures to interact with the 3D model

### Adding New Scenes
1. Create a new folder (e.g., `46/`)
2. Add 3D model to `46/obj/`
3. Add QR pattern to `46/qr/`
4. Create `index.html` and `image-tracking.html` based on existing scenes
5. Link to shared scripts from `common/`
6. Update main `index.html` to include the new scene

## Deployment

### GitHub Pages Automatic Deployment

This project is configured for automatic deployment to GitHub Pages on every commit.

**Setup Instructions:**

1. **Push code to GitHub:**
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```

2. **Enable GitHub Pages in your repository:**
   - Go to your GitHub repository
   - Click **Settings** → **Pages**
   - Under **Build and deployment**:
     - **Source**: Select "GitHub Actions"
   - Save the settings

3. **Automatic deployment:**
   - Every push to `main` or `master` branch triggers automatic deployment
   - GitHub Actions workflow (`.github/workflows/deploy.yml`) handles the build and deployment
   - Your site will be available at: `https://[username].github.io/[repository-name]/`
   - Deployment takes 1-2 minutes after each commit

4. **Monitor deployment:**
   - Check the **Actions** tab in your GitHub repository
   - You'll see the deployment workflow running
   - Green checkmark = successful deployment
   - Red X = deployment failed (check logs for details)

**How it works:**
- The workflow automatically triggers on commits to main/master branches
- All project files are uploaded as-is (static HTML deployment)
- No build process needed - `index.html` serves as the entry point
- GitHub Pages provides HTTPS automatically for AR camera access

### Static File Serving (Replit Development)
- The application is served as static files
- No backend processing required
- All AR processing happens client-side in the browser

### Production Considerations
- HTTPS required for camera access on most devices (GitHub Pages provides this automatically)
- Ensure all CDN resources are accessible
- Test on mobile devices for best AR experience
- QR codes should be printed clearly for reliable tracking

## User Preferences
- No specific preferences recorded yet

## Maintenance Notes

### Common Scripts
All scenes use shared scripts from `/common/`:
- `gesture-detector.js` - handles touch input detection
- `gesture-handler.js` - processes gestures for AR models
- `styles.css` - base styling for AR interface

### Cleanup Automation
Use `cleanup_ar_folders.py` to:
- Remove duplicate scripts from individual scene folders
- Update HTML files to use shared common/ scripts
- Maintain consistent structure across all scenes

### Dependencies
- A-Frame (loaded via CDN)
- AR.js (loaded via CDN)
- AR.js NFT version (for image tracking)
- aframe-extras (for animation support)

## Browser Compatibility
- Modern browsers with WebXR support
- Mobile devices recommended for best AR experience
- Camera permissions required
- HTTPS connection required in production

## Resources
- [A-Frame Documentation](https://aframe.io/docs/)
- [AR.js Documentation](https://ar-js-org.github.io/AR.js-Docs/)
- See `README.md` for Russian documentation
- See `DEVELOPER.md` for development guidelines
