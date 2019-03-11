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

const OverturnRateByLevel = ({ data }) => {
  return (
    <WrappedColumns
      category='denial_category'
      data={data}
      field='overturn_rate'
      filter={filter}
      groupBy='level'
      label='percent'
    />
  );
};

OverturnRateByLevel.propTypes = {
  data: PropTypes.array.isRequired
};

export default OverturnRateByLevel;
