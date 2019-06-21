import React from 'react';
import PropTypes from 'prop-types';
import { colorByLevel, colorIfNegative } from '../utils/colors';
import { formatLabel } from '../utils/formatting';

const StackedDataColumns = ({ data, groupBy, field }) => {
  const dataRows = Object.keys(data[0][field]).map((k,i) => {
    return (
      <div
        className="ds-u-justify-content--center ds-u-align-items--baseline ds-u-display--flex"
        key={`${groupBy}-${field}-${k}`}
      >
        <h4 className="ds-u-font-weight--normal ds-u-text-align--center ds-u-margin-y--1 ds-u-color--muted">
          {k.replace('_', ' ')}
        </h4>
      </div>
    );
  });

  const dataColumns = data.map((record, idx) => {
    const values = Object.keys(record[field]).map((k, i) => {
      return (
        <div
          key={`${record[groupBy]}-${k}-${i}`}
          className="ds-u-justify-content--center ds-u-align-items--baseline ds-u-display--flex"
        >
          <h4 className="ds-u-text-align--center ds-u-margin-y--1">
            {`${record[field][k]}`}
          </h4>
          <h6 className="ds-u-color--muted ds-u-margin-y--1">%</h6>
        </div>
      );
    });

    return (
      <div
        className={`
          ds-u-margin-y--2
          ds-u-padding-y--3
          ds-col
        `}
        key={`column-${groupBy}-${idx}`}
      >
        <div className="ds-u-padding-x--1 ds-u-padding-bottom--3">
          <div
            className="ds-u-justify-content--center ds-u-align-items--center ds-u-display--flex"
          >
            <div
              className="ds-u-align-items--center ds-u-display--flex"
              style={{
                borderBottom: '6px solid',
                borderColor: colorByLevel(record[groupBy]),
                verticalAlign: 'bottom'
              }}
            >
              <p className="ds-u-margin-right--1 ds-u-color--muted ds-u-margin--0">
              {`${formatLabel(groupBy)}`}
              </p>
              <p className="ds-u-font-weight--bold ds-u-margin--0">
              {`${record[groupBy]}`}
              </p>
            </div>
          </div>
        </div>
        {values}
      </div>
    )
  });

  return (
    <div className="ds-l-row ds-u-justify-content--between">
      <div
        className={`
          ds-u-margin-y--2
          ds-u-padding-y--3
          ds-col
        `}
      >
        <div className="ds-u-padding-x--1 ds-u-padding-bottom--3">
          <div
            className="ds-u-justify-content--center ds-u-align-items--center ds-u-display--flex"
          >
            <div
              className="ds-u-align-items--center ds-u-display--flex"
              style={{
                borderBottom: '6px solid',
                verticalAlign: 'bottom'
              }}
            >
              <p className="ds-u-color--muted ds-u-margin--0">
              {`${formatLabel('Category')}`}
              </p>
            </div>
          </div>
        </div>
        {dataRows}
      </div>
      {dataColumns}
    </div>
  );
}

StackedDataColumns.propTypes = {
  data: PropTypes.array.isRequired,
  groupBy: PropTypes.string.isRequired,
  label: PropTypes.string.isRequired
};

export default StackedDataColumns;
