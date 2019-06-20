import React from 'react';
import PropTypes from 'prop-types';
import { colorByLevel } from '../utils/colors';
import { formatLabel } from '../utils/formatting';

const TableRow = ({ record, groupBy, field, fieldLabel }) => {
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
        style={{
          borderLeft: '6px solid',
          borderColor: colorByLevel(record[groupBy]),
          verticalAlign: 'bottom'
        }}
      >
        <div
          className={`
            ds-u-justify-content--center
            ds-u-align-items--center
            ds-u-display--flex
            ds-u-sm-font-size--small
            ds-u-md-font-size--small
            ds-u-lg-font-size--base
          `}
        >
          <p className="ds-u-margin-x--1 ds-u-color--muted ds-u-margin--0">
          {`${formatLabel(groupBy)}`}
          </p>
          <p className="ds-u-font-weight--bold ds-u-margin--0">
          {`${record[groupBy]}`}
          </p>
        </div>
      </div>
      <div>
        <div className="ds-u-justify-content--end ds-u-align-items--baseline ds-u-display--flex">
          <p
            className={`
              ds-u-font-weight--bold
              ds-u-margin--0
              ds-u-sm-font-size--h4
              ds-u-md-font-size--h4
              ds-u-lg-font-size--h3
              ds-u-xl-font-size--h2
            `}
          >
          {`${record[field].toLocaleString()}`}
          </p>
          <p className="ds-u-margin-x--1 ds-u-color--muted ds-u-font-size--tiny ds-u-margin--0">
          {`${formatLabel(fieldLabel || field)}`}
          </p>
        </div>
      </div>
    </div>
  )
}

const TableView = ({ data, groupBy, field, fieldLabel, category }) => {
  const tableRows = data.map((record, idx) => {
    return (
      <TableRow
        record={record}
        groupBy={groupBy}
        field={field}
        fieldLabel={fieldLabel}
        key={`table-row-${groupBy}-${field}-${idx}`}
      />
    );
  });

  return (
    <div className={`
        ds-l-col--12
        ds-u-sm-padding-x--1
        ds-u-md-padding-x--2
        ds-u-lg-padding-x--3
        ds-u-padding-top--5
        ds-u-sm-padding-top--5
        ds-u-md-padding-top--6
        ds-u-lg-padding-top--7
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
  fieldLabel: PropTypes.string,
  category: PropTypes.string
}

export default TableView;
