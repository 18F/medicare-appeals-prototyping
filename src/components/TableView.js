import React from 'react';
import PropTypes from 'prop-types';
import colorByLevel from '../utils/colorByLevel';
import { formatLabel } from '../utils/formatting';

const TableRow = ({ record, groupBy, field }) => {
  return (
    <div
      className={`
        ds-u-justify-content--between
        ds-u-align-items--center
        ds-u-display--flex
        ds-u-margin-y--2
        ds-u-border-bottom--1
      `}
    >
      <div
        className="ds-u-padding-x--1"
        style={{
          borderLeft: '6px solid',
          borderColor: colorByLevel(record[groupBy]),
          verticalAlign: 'bottom'
        }}
      >
        <div className="ds-u-justify-content--center ds-u-align-items--center ds-u-display--flex">
          <p className="ds-u-margin-x--1 ds-u-color--muted ds-u-margin--0">
          {`${formatLabel(groupBy)}`}
          </p>
          <p className="ds-u-font-weight--bold ds-u-margin--0">
          {`${record[groupBy]}`}
          </p>
        </div>
      </div>
      <div className="ds-u-padding-x--1">
        <div className="ds-u-justify-content--center ds-u-align-items--center ds-u-display--flex">
          <p className="ds-u-font-weight--bold ds-u-font-size--h3 ds-u-margin--0">
          {`${record[field].toLocaleString()}`}
          </p>
          <p className="ds-u-margin-x--1 ds-u-color--muted ds-u-font-size--small ds-u-margin--0">
          {`${formatLabel(field)}`}
          </p>
        </div>
      </div>
    </div>
  )
}

const TableView = ({ data, groupBy, field, category }) => {
  const tableRows = data.map((record, idx) => {
    return (
      <TableRow
        record={record}
        groupBy={groupBy}
        field={field}
        key={`table-row-${groupBy}-${field}-${idx}`}
      />
    );
  });

  return (
    <div className={`
        ds-l-col--12
        ds-u-sm-padding-x--2
        ds-u-md-padding-x--3
        ds-u-lg-padding-x--7
        ds-u-margin-top--3
        ds-u-margin-bottom--2
      `}
    >
      {tableRows}
    </div>
  );
}

TableView.propTypes = {
  data: PropTypes.array,
  groupBy: PropTypes.string,
  field: PropTypes.string,
  category: PropTypes.string
}

export default TableView;
