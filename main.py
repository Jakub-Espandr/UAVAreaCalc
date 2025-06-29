import sys
import os
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont

# Suppress Qt warnings and threading issues on macOS
os.environ['QT_MAC_WANTS_LAYER'] = '1'
os.environ['QT_LOGGING_RULES'] = 'qt.qpa.*=false;qt.*=false'
os.environ['QT_LOGGING_RULES'] = '*.debug=false;qt.*=false'

# Suppress specific macOS warnings
if sys.platform == 'darwin':
    os.environ['QT_MAC_WANTS_LAYER'] = '1'
    # Suppress NSOpenPanel warnings
    os.environ['QT_MAC_DISABLE_ACCESSIBILITY'] = '1'
    # Suppress threading warnings
    os.environ['QT_THREAD_PRIORITY_POLICY'] = '1'
    # Suppress all Qt warnings
    os.environ['QT_LOGGING_RULES'] = '*.debug=false;qt.*=false;*.info=false'

# Import the refactored UI and resource functions
from ui.main_window import UAVAreaCalculator
from utils.resources import get_app_icon, load_custom_fonts

def main():
    """
    Main function to initialize and run the UAV Area Calculator application.
    """
    app = QApplication(sys.argv)
    
    # Load custom fonts and set default for the application
    load_custom_fonts()
    app.setFont(QFont("fccTYPO", 11))

    # Set default font for matplotlib plots to match
    plt.rcParams['font.family'] = 'fccTYPO'
    
    # Load and set the application icon
    app_icon = get_app_icon()
    if app_icon:
        app.setWindowIcon(app_icon)

    # Create and show the main window
    window = UAVAreaCalculator(app_icon=app_icon)
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
