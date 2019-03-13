import React from 'react';
import PropTypes from 'prop-types';

const SelectView = ({disabled, name, options, selected, title, setState}) => {
  const optionList = options.map((val, idx) => {
    return (
      <option value={val} key={`${val}-${idx}`}>
        {val.charAt(0).toUpperCase() + val.slice(1)}
      </option>
    );
  });

  return (
    <div className="ds-l-col--auto ">
        <label className="ds-c-label ds-u-margin--0" htmlFor="graph-select">
          <span
            className={`
              ds-c-field__hint
              ds-u-font-size--small
              ds-u-lg-font-size--base
            `}
          >
            {title}
          </span>
        </label>
        <select
          disabled={disabled}
          value={selected}
          className={`
            ds-c-field
            ds-u-padding-y--1
            ds-u-border--2
            ds-u-font-size--small
            ds-u-lg-font-size--base
          `}
          onChange={(e) => setState(e.target.value, name)}
        >
          { optionList }
        </select>
    </div>
  );
};

SelectView.propTypes = {
  disabled: PropTypes.bool,
  name: PropTypes.string,
  options: PropTypes.array,
  selected: PropTypes.string,
  title: PropTypes.string,
  setState: PropTypes.func,
}

SelectView.defaultProps = {
  disabled: false,
  options: ['option-1', 'option-2'],
  name: 'select-view',
  selected: 'option-1',
  title: 'Select Option',
  setState: (val) => console.log(val),
}

export default SelectView;
