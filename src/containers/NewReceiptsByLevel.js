import React from 'react';
import PropTypes from 'prop-types';
import graphContainer from '../components/GraphContainer';
import BarChart from '../components/BarChart';
import dashboard from '../selectors/dashboard';

const filter = {
  options: ['all', 'non-rac', 'rac'],
  selected: 'all',
  title: 'Filters'
}

const WrappedGraph = graphContainer(BarChart, dashboard)

const NewReceipts = ({ data }) => {
  return (
    <WrappedGraph
      data={data}
      groupBy='level'
      category='denial_category'
      field='receipts'
      filter={filter}
    />
  );
};

NewReceipts.propTypes = {
  data: PropTypes.array
};

export default NewReceipts;
