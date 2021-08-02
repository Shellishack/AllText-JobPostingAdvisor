import {process_stream} from './processstream.js';
import {shownext, print_sessionstorage, showprevious} from './readstorage.js';

// process_stream(str) takes a string that contains job requirements.
// Then it parses the string into a list of sentences, and it posts the sentences to Azure.
// Finally it stores results in sessionStorage
window.process_stream=process_stream;

// shownext(elementid) takes a html element id, then it shows the next result (a sentence with labels given by AI) in specified element.
//*this function needs to be modified slightly depending on the UI.
window.shownext=shownext;

// showprevious(elementid) takes a html element id, then it shows the previous result (a sentence with labels given by AI) in the specified element.
//*this function needs to be modified slightly depending on the UI.
window.showprevious=showprevious;

// print_sessionstorage() prints the storage.
// Used for debugging.
window.print_sessionstorage=print_sessionstorage;