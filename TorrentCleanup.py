#!/usr/bin/env python
"""

    #########################################################################
    # Title:         Torrent Cleanup Script                                 #
    # Author(s):     l3uddz                                                 #
    # URL:           https://github.com/cloudbox/cloudbox                   #
    # Description:   Cleanup auto extracted files in ruTorrent downloads.   #
    # --                                                                    #
    #         Part of the Cloudbox project: https://cloudbox.works          #
    #########################################################################
    #                   GNU General Public License v3.0                     #
    #########################################################################

"""
import logging
import os
import sys

# Setup logger
log_filename = os.path.join(os.path.dirname(sys.argv[0]), 'cleanup.log')
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s'
)
log = logging.getLogger("TorrentCleanup")

# Retrieve Required Variables
if os.environ.get('sonarr_eventtype') == "Test":
    sys.exit(0)
elif 'sonarr_eventtype' in os.environ:
    sourceFile = os.environ.get('sonarr_episodefile_sourcepath')
    sourceFolder = os.environ.get('sonarr_episodefile_sourcefolder')
elif 'radarr_eventtype' in os.environ:
    sourceFile = os.environ.get('radarr_moviefile_sourcepath')
    sourceFolder = os.environ.get('radarr_moviefile_sourcefolder')
elif 'lidarr_eventtype' in os.environ:
    sourceFile = os.environ.get('lidarr_trackfile_path')
    sourceFolder = os.environ.get('lidarr_addedtrackpaths')
else:
    log.error("Unable to determine cleanup requester. This must be either 'sonarr', 'radarr', or 'lidarr'.")
    sys.exit(0)

if os.path.exists(sourceFile) and os.path.isfile(sourceFile):
    # Scan folder for rar, if rar exists, remove sourceFile
    for found_file in os.listdir(sourceFolder):
        if found_file.endswith(".rar"):
            os.remove(sourceFile)
            log.info("Purged '%s'", sourceFile)
            break
