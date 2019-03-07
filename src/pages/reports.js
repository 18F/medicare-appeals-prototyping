import '@babel/polyfill';

import React from 'react';
import ReactDOM from 'react-dom';
import ReportNewReceipts from '../components/ReportNewReceipts';
import ReportDispositions from '../components/ReportDispositions';

const reports = (context) => {
  ReactDOM.render(
    <ReportNewReceipts data={context} />,
    document.getElementById('new-receipt-report')
  );

  ReactDOM.render(
    <ReportDispositions data={context} />,
    document.getElementById('dispositions-report')
  );

  ReactDOM.render(
    <ReportDispositions data={context} />,
    document.getElementById('net-appeal-report')
  );

  ReactDOM.render(
    <ReportDispositions data={context} />,
    document.getElementById('rac-report')
  );
}

export default {
  reports
};
