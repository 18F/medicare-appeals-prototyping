import '@babel/polyfill';

import React from 'react';
import ReactDOM from 'react-dom';
import NewReceipts from '../components/GraphNewReceipts';
import DispositionsByLevel from '../components/GraphDispositionsByLevel';
import GraphWIPByLevel from '../components/GraphWIPByLevel';

const dashboard = (context) => {
  ReactDOM.render(
    <NewReceipts data={context} />,
    document.getElementById('new-receipts-by-hhs-level')
  );

  ReactDOM.render(
    <DispositionsByLevel data={context} />,
    document.getElementById('dispositions-by-hhs-level')
  );

  ReactDOM.render(
    <GraphWIPByLevel data={context} />,
    document.getElementById('work-in-progress-by-hhs-level')
  );
};

export default {
  dashboard
};
