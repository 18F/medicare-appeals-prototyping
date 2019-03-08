import '@babel/polyfill';

import React from 'react';
import ReactDOM from 'react-dom';
import NewReceiptsByLevel from '../containers/NewReceiptsByLevel';
import DispositionsByLevel from '../containers/DispositionsByLevel';
import WIPByLevel from '../containers/WIPByLevel';

const initialState = [
  {level: 1, receipts: 1021, dispositions: 1030, work_in_progress: 60, denial_category: 'rac'},
  {level: 1, receipts: 8021, dispositions: 10030, work_in_progress: 787, denial_category: 'non-rac'},
  {level: 2, receipts: 500, dispositions: 401, work_in_progress: 101, denial_category: 'rac'},
  {level: 2, receipts: 4500, dispositions: 4010, work_in_progress: 510, denial_category: 'non-rac'},
  {level: 3, receipts: 401, dispositions: 502, work_in_progress: 20, denial_category: 'rac'},
  {level: 3, receipts: 3500, dispositions: 3321, work_in_progress: 200, denial_category: 'non-rac'},
  {level: 4, receipts: 201, dispositions: 220, work_in_progress: 50, denial_category: 'rac'},
  {level: 4, receipts: 2900, dispositions: 3200, work_in_progress: 100, denial_category: 'non-rac'}
];

const dashboard = (context) => {
  const data = context || initialState;

  ReactDOM.render(
    <NewReceiptsByLevel data={data} />,
    document.getElementById('new-receipts-by-hhs-level')
  );

  ReactDOM.render(
    <DispositionsByLevel data={data} />,
    document.getElementById('dispositions-by-hhs-level')
  );

  ReactDOM.render(
    <WIPByLevel data={data} />,
    document.getElementById('work-in-progress-by-hhs-level')
  );
};

export default {
  dashboard
};
