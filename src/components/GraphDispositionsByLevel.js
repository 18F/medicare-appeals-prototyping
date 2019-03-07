import React from 'react';
import PropTypes from 'prop-types';
import graphContainer from './GraphContainer';
import BarChart from './BarChart';

const initialState = [
  {level: 1, receipts: 13021},
  {level: 2, receipts: 8305},
  {level: 3, receipts: 6780},
  {level: 4, receipts: 4422}
];

const WrappedGraph = graphContainer(BarChart);

const DispositionsByLevel = ({ data }) => (<WrappedGraph data={data} />);

DispositionsByLevel.propTypes = {
  data: PropTypes.array
};

DispositionsByLevel.defaultProps = {
  data: initialState
};

export default DispositionsByLevel;
