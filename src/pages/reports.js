import '@babel/polyfill';

import React from 'react';
import ReactDOM from 'react-dom';
import NewReceiptsByLevel from '../containers/NewReceiptsByLevel';
import DispositionsByLevel from '../containers/DispositionsByLevel';
import Glossary from '../containers/Glossary';
import { dashboardContext } from '../constants';

const reports = (context=dashboardContext) => {
  ReactDOM.render(
    <Glossary />,
    document.getElementById('glossary-button')
  );

  ReactDOM.render(
    <DispositionsByLevel data={context} />,
    document.getElementById('new-receipt-report')
  );

  ReactDOM.render(
    <NewReceiptsByLevel data={context} />,
    document.getElementById('dispositions-report')
  );

  ReactDOM.render(
    <NewReceiptsByLevel data={context} />,
    document.getElementById('net-appeal-report')
  );

  ReactDOM.render(
    <DispositionsByLevel data={context} />,
    document.getElementById('rac-report')
  );
}

export default {
  reports
};
