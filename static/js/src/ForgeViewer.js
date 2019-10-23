/* eslint-disable no-console */
/* global console */
/* global window */
/* global document */
/* global Autodesk */
/* global Event */
/**
 * Wrapper class for Forge Viewer creation
 */
export default class ForgeViewer {
  /**
   * Initialize a viewer
   * @param {string} documentId Forge svf document
   * @param {string} accessToken Forge Auth token
   * @param {string} viewerSection html element id
   * @param {boolean} shouldShowEvents log Forge dispatched events
   * @param {object} viewerConfig config object for GuiViewer3D init
   */
  constructor(
      documentId,
      accessToken,
      viewerSection,
      shouldShowEvents = false,
      viewerConfig = {}) {
    this._viewer = null;
    this._accessToken = accessToken;
    this._viewerSection = viewerSection;
    this._shouldShowEvents = shouldShowEvents;
    this._viewerConfig = viewerConfig;
    this.documentId = documentId;
    this.VIEWER_READY = 'forgeViewerReady';

    this.create();
  }

  /**
   * Initializes the Viewer
   */
  create() {
    const options = {
      env: 'AutodeskProduction',
      accessToken: this._accessToken,
    };
    // eslint-disable-next-line new-cap
    Autodesk.Viewing.Initializer(options, () => {
      const currentViewer = this;
      window.forgeViewer = currentViewer;
      Autodesk.Viewing.Document.load(
          currentViewer.documentId,
          (doc) => currentViewer._docLoadSuccess(doc),
          (doc) => currentViewer._docLoadFailed(doc)
      );
    });
  }

  /**
   * Updates the viewer to a new document
   * @param {string} documentId Forge model documentId
   */
  navigate(documentId) {
    this._viewer.tearDown();
    this.documentId = documentId;
    this.create();
  }

  /**
   * This method allows us to see all of the events
   * that the Forge viewer raises
   */
  _subscribeToAllEvents() {
    for (const key in Autodesk.Viewing) {
      if (key.endsWith('_EVENT')) {
        this._viewer.addEventListener(
            Autodesk.Viewing[key],
            function(event) {
              console.log(key, event);
            }
        );
      }
    }
  }
  /**
   * Forge document loaded
   * doc is svf address resource
   * @param {Document} doc Forge document
   */
  _docLoadSuccess(doc) {
    console.log(this);
    // A document contains references to 3D and 2D geometries.
    const geometries = doc.getRoot().search({'type': 'geometry'});
    if (geometries.length === 0) {
      console.log('Document has no geometry');
      return;
    }

    // Choose any of the avialable geometries
    const initGeom = geometries[0];

    // Create Viewer instance
    const viewerDiv = document.getElementById(this._viewerSection);
    this._viewer = new Autodesk.Viewing.Private.GuiViewer3D(
        viewerDiv,
        this._viewerConfig
    );

    // Load the chosen geometry
    const svfUrl = doc.getViewablePath(initGeom);
    const modelOptions = {
      sharedPropertyDbPath: doc.getPropertyDbPath(),
    };
    const currentViewer = this;
    this._viewer.start(
        svfUrl,
        modelOptions,
        (data) => currentViewer._modelLoadSuccess(data),
        (data) => currentViewer._modelLoadFailed(data)
    );
  }

  /**
   * Model Loads, not necessarily the geometry of the model
   */
  _modelLoadSuccess() {
    console.log('Model Loaded!');
    window.dispatchEvent(new Event(this.VIEWER_READY));
    if (this._shouldShowEvents) {
      this._subscribeToAllEvents();
    }
  }

  /**
   * Forge document failed to load
   * doc is svf address resource
   */
  _docLoadFailed() {
    console.log('Failed to load document.');
    console.log('Check documentId and token are valid.');
  }

  /**
   * svf model failed to load
   */
  _modelLoadFailed() {
    console.log('Failed to load model.');
  }
}
