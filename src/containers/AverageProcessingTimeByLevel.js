import React from 'react';
import PropTypes from 'prop-types';
import columnContainer from '../components/ColumnContainer';
import DataColumns from '../components/DataColumns';
import averageAmount from '../selectors/averageAmount';

const filter = {
  options: ['all', 'non-rac', 'rac'],
  selected: 'all',
  title: 'Filters'
}

const WrappedColumns = columnContainer(DataColumns, averageAmount);

const AverageProcessingTime = ({ data }) => {
  return (
    <WrappedColumns
      category='denial_category'
      data={data}
      field='days'
      filter={filter}
      groupBy='level'
      label='days'
    />
  );
};

AverageProcessingTime.propTypes = {
  data: PropTypes.array.isRequired
};

export default AverageProcessingTime;
