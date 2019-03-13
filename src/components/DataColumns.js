import React from 'react';
import PropTypes from 'prop-types';
import { colorByLevel, colorIfNegative } from '../utils/colors';
import { formatLabel } from '../utils/formatting';

const DataColumns = ({ data, groupBy, label, }) => {
  const dataColumns = data.map((record, idx) => {
    return (
      <div
        className={`
          ds-u-margin-y--2
          ds-u-padding-y--3
          ds-u-border-right--1
          ds-u-border-left--1
          ds-l-sm-col--12
          ds-l-md-col--6
          ds-l-lg-col--3
          ds-l-xl-col--3
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
        <div
          className="ds-u-justify-content--center ds-u-align-items--baseline ds-u-display--flex"
        >
          <h1
            style={{
              color: colorIfNegative(record[label])
            }}
            className="ds-display ds-u-text-align--center"
          >
            {`${record[label].toLocaleString()}`}
          </h1>
        </div>
        <div
          className="ds-u-justify-content--center ds-u-align-items--baseline ds-u-display--flex"
        >
          <p className="ds-u-margin-x--1 ds-u-color--muted ds-u-font-size--small ds-u-margin--0">
          {`${formatLabel(label)}`}
          </p>
        </div>
      </div>
    )
  });

  return (
    <div className="ds-l-row">
      {dataColumns}
    </div>
  );
}

DataColumns.propTypes = {
  data: PropTypes.array.isRequired,
  groupBy: PropTypes.string.isRequired,
  label: PropTypes.string.isRequired
};

export default DataColumns;
