import '@babel/polyfill';

import React from 'react';
import ReactDOM from 'react-dom';
import NewReceiptsByLevel from '../containers/NewReceiptsByLevel';
import DispositionsByLevel from '../containers/DispositionsByLevel';
import WIPByLevel from '../containers/WIPByLevel';
import NetReceiptsByLevel from '../containers/NetReceiptsByLevel';
import AverageProcessingTime from '../containers/AverageProcessingTimeByLevel';
import OverturnRateByLevel from '../containers/OverturnRateByLevel';
import { dashboardContext } from '../constants';

const dashboard = (context=dashboardContext) => {
  ReactDOM.render(
    <NewReceiptsByLevel data={context} />,
    document.getElementById('new-receipts-by-hhs-level')
  );

  ReactDOM.render(
    <DispositionsByLevel data={context} />,
    document.getElementById('dispositions-by-hhs-level')
  );

  ReactDOM.render(
    <WIPByLevel data={context} />,
    document.getElementById('work-in-progress-by-hhs-level')
  );

  ReactDOM.render(
    <NetReceiptsByLevel data={context} />,
    document.getElementById('net-receipts-by-level')
  );

  ReactDOM.render(
    <AverageProcessingTime data={context} />,
    document.getElementById('average-processing-time')
  );

  ReactDOM.render(
    <OverturnRateByLevel data={context} />,
    document.getElementById('total-overturn-rate')
  );
};

export default {
  dashboard
};
