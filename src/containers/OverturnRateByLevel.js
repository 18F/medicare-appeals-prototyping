import React from 'react';
import PropTypes from 'prop-types';
import stackedColumnContainer from '../components/StackedColumnContainer';
import StackedDataColumns from '../components/StackedDataColumns';
import fieldFilter from '../selectors/fieldFilter';

const filter = {
  options: ['all', 'non-rac', 'rac'],
  selected: 'all',
  title: 'Filters'
}

const WrappedColumns = stackedColumnContainer(StackedDataColumns, fieldFilter);

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
