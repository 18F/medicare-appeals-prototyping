import React from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';
import { navigate } from '@reach/router';
import fetch from 'cross-fetch';
import { Dialog, Pane } from 'evergreen-ui';
import { DateRange } from 'react-date-range';
import { queryDate, readDate } from '../utils/formatting';
import { getDateRange } from '../utils/url';

import NewReceiptsByLevel from '../containers/NewReceiptsByLevel';
import DispositionsByLevel from '../containers/DispositionsByLevel';
import WIPByLevel from '../containers/WIPByLevel';
import NetReceiptsByLevel from '../containers/NetReceiptsByLevel';
import AverageProcessingTime from '../containers/AverageProcessingTimeByLevel';
import OverturnRateByLevel from '../containers/OverturnRateByLevel';

import 'react-date-range/dist/styles.css';
import 'react-date-range/dist/theme/default.css';

const NewReceiptsByLevelPortal = ({ data }) => (
  ReactDOM.createPortal(
    <NewReceiptsByLevel data={data} />,
    document.getElementById('new-receipts-by-hhs-level')
  )
);

const DispositionsByLevelPortal = ({ data }) => (
  ReactDOM.createPortal(
    <DispositionsByLevel data={data} />,
    document.getElementById('dispositions-by-hhs-level')
  )
);

const WIPByLevelPortal = ({ data }) => (
  ReactDOM.createPortal(
    <WIPByLevel data={data} />,
    document.getElementById('work-in-progress-by-hhs-level')
  )
);

const NetReceiptsByLevelPortal = ({ data }) => (
  ReactDOM.createPortal(
    <NetReceiptsByLevel data={data} />,
    document.getElementById('net-receipts-by-level')
  )
);

const AverageProcessingTimePortal = ({ data }) => (
  ReactDOM.createPortal(
    <AverageProcessingTime data={data} />,
    document.getElementById('average-processing-time')
  )
);

const OverturnRateByLevelPortal = ({ data }) => (
  ReactDOM.createPortal(
    <OverturnRateByLevel data={data} />,
    document.getElementById('total-overturn-rate')
  )
);


class DateRangePicker extends React.Component {
  constructor(props) {
    super(props);

    const range = getDateRange(props.start, props.end);

    this.state = {
      isShown: false,
      data: props.data,
      end: range.end,
      start: range.start,
      range: {
        endDate: range.end,
        startDate: range.start
      }
    };

    this.setState = this.setState.bind(this);
    this.cancelSelect = this.cancelSelect.bind(this);
    this.confirmSelect = this.confirmSelect.bind(this);
    this.dateSelect = this.dateSelect.bind(this);
    this.fetchData = this.fetchData.bind(this);
  }

  cancelSelect() {
    const { end, start } = this.state;

    this.setState({
      isShown: false,
      range: {
        endDate: end,
        startDate: start,
      }
    });
  }

  confirmSelect() {
    const { end, range, start } = this.state;
    const endOld = queryDate(end);
    const startOld = queryDate(start);
    const endNew = queryDate(range.endDate);
    const startNew = queryDate(range.startDate);

    if ((endNew === endOld) && (startNew === startOld)) {
      return this.setState({
        isShown: false,
      });
    }

    const { pathname } = window.location;
    const queryParams = `?start=${startNew}&end=${endNew}`;

    return this.fetchData(queryParams)
      .then(data => {
        this.setState({
          data,
          isShown: false,
          end: range.endDate,
          start: range.startDate,
        });

        navigate(`${pathname}${queryParams}`)
      });
  }

  dateSelect(event) {
    const { range1 } = event;
    this.setState({
      range: range1
    });
  }

  fetchData(url) {
    return fetch(`/api/overview/${url}`)
      .then(res => {
        if (res.status >= 400) {
          return new Error('Error retrieving data.');
        }

        return res.json();
      })
      .catch(console.log)
  }

  render() {
    const { cancelSelect, confirmSelect, dateSelect, setState, state } = this;
    const { data, end, start, isShown, range } = state;

    return (
      <React.Fragment>
        <Pane>
          <Dialog
            isShown={isShown}
            title="Select search dates"
            hasHeader={false}
            onCloseComplete={() => setState({ isShown: false })}
            confirmLabel="Confirm"
            onCancel={cancelSelect}
            onConfirm={confirmSelect}
          >
            <Pane
              display="flex"
              alignItems="center"
              justifyContent="center"
              border="default"
              className="ds-u-padding-y--1"
            >
              <DateRange
                onChange={dateSelect}
                moveRangeOnFirstSelection={true}
                ranges={[{
                  startDate: new Date(range.startDate),
                  endDate: new Date(range.endDate)
                }]}
                className={'PreviewArea'}
                shownDate={new Date(range.endDate)}
                maxDate={this.props.maxDate}
              />
            </Pane>
          </Dialog>
            <button
              type="button"
              className={`
                ds-c-button
                ds-u-float--right
                ds-u-fill--white
              `}
              onClick={() => { setState({isShown: true})}}
              >
                <p className="ds-u-font-size--small">
                  {readDate(start)} <span className="ds-u-font-weight--normal">to</span> {readDate(end)}
                </p>
            </button>
        </Pane>
        <NewReceiptsByLevelPortal data={data} />
        <DispositionsByLevelPortal data={data} />
        <WIPByLevelPortal data={data} />
        <NetReceiptsByLevelPortal data={data} />
        <AverageProcessingTimePortal data={data} />
        <OverturnRateByLevelPortal data={data} />
      </React.Fragment>
    );
  }
};

DateRangePicker.defaultProps = {
  date: [],
  end: new Date(Date.now()),
  start: new Date('2010-01-01'),
  maxDate: new Date(Date.now())
}

DateRangePicker.propTypes = {
  data: PropTypes.array,
  end: PropTypes.instanceOf(Date),
  start: PropTypes.instanceOf(Date),
  maxDate: PropTypes.instanceOf(Date)
}

export default DateRangePicker;
