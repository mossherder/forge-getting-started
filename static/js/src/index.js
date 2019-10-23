/* global document */
/* global window */
/* global Autodesk */
import ForgeViewer from './ForgeViewer.js';

const forgeViewerDivId = 'forge-viewer'; //HTML Element Id

const viewerConfig = {
  'extensions': []
};

const getModelData = $.ajax({
  url: '/model',
  type: 'POST',
});

getModelData.done(function(data) {
  const viewer = new ForgeViewer(
      data['documentId'],
      data['accessToken'],
      forgeViewerDivId,
      false,
      null // can replace with viewerConfig
  );
  window.addEventListener(viewer.VIEWER_READY, () => {console.log('Viewer Ready - Model Loaded')},
  {
    'once': true,
  });
});
