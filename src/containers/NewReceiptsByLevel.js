import React from 'react';
import PropTypes from 'prop-types';
import graphContainer from '../components/GraphContainer';
import BarChart from '../components/BarChart';
import TableView from '../components/TableView';
import sumAmount from '../selectors/sumAmount';

const filter = {
  options: ['all', 'non-rac', 'rac'],
  selected: 'all',
  title: 'Filters'
}

const view = {
  options: ['graph', 'table'],
  selected: 'table',
  title: 'Select View'
}

const WrappedGraph = graphContainer(BarChart, TableView, sumAmount)

const NewReceipts = ({ data }) => {
  return (
    <WrappedGraph
      category='denial_category'
      data={data}
      field='receipts'
      filter={filter}
      groupBy='level'
      view={view}
    />
  );
};

NewReceipts.propTypes = {
  data: PropTypes.array.isRequired
};

export default NewReceipts;
