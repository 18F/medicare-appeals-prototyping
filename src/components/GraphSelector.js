import React from 'react';
import PropTypes from 'prop-types';

const defaultOptions = ['All', 'RAC', 'Non-RAC']

const GraphSelector = ({options}) => {
  const optionList = options.map((val, idx) => <option value={val} key={`${val}-${idx}`}>{val}</option>)

  return (
    <div className="ds-l-row ds-u-justify-content--end">
        <div className="ds-l-col--auto ">
            <label className="ds-c-label ds-u-margin--0" htmlFor="graph-select">
              <span className="ds-c-field__hint">Filter</span>
            </label>
            <select disabled className="ds-c-field ds-u-padding-y--0 ds-u-border--2">
              { optionList }
            </select>
        </div>
    </div>
  );
};

GraphSelector.propTypes = {
  options: PropTypes.array
}

GraphSelector.defaultProps = {
  options: defaultOptions
}

export default GraphSelector;
