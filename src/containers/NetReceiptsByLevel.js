import React from 'react';
import PropTypes from 'prop-types';
import columnContainer from '../components/ColumnContainer';
import DataColumns from '../components/DataColumns';
import netAmounts from '../selectors/netAmounts';

const filter = {
  options: ['all', 'non-rac', 'rac'],
  selected: 'all',
  title: 'Filters'
}

const WrappedColumns = columnContainer(DataColumns, netAmounts)

const NetReceipts = ({ data }) => {
  return (
    <WrappedColumns
      category='denial_category'
      data={data}
      difference='appeals'
      filter={filter}
      groupBy='level'
      label='appeals'
      minuend='dispositions'
      subtrahend='receipts'
    />
  );
};

NetReceipts.propTypes = {
  data: PropTypes.array.isRequired
};

export default NetReceipts;
