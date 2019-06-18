import '@babel/polyfill';

import React from 'react';
import ReactDOM from 'react-dom';
import DateRange from '../containers/DateRange';
import Glossary from '../containers/Glossary';
import { dashboardContext } from '../constants';

const dashboard = (context=dashboardContext) => {
  ReactDOM.render(
    <Glossary />,
    document.getElementById('glossary-button')
  );

  ReactDOM.render(
    <DateRange data={context} />,
    document.getElementById('date-range-picker')
  );
};

export default {
  dashboard
};
