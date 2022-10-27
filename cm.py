import queue
from fritzconnection.core.fritzmonitor import FritzMonitor

def process_events(monitor, event_queue, healthcheck_interval=10):
    while True:
        try:
            event = event_queue.get(timeout=healthcheck_interval)
        except queue.Empty:
            # check health:
            if not monitor.is_alive:
                raise OSError("Error: fritzmonitor connection failed")
        else:
            # do event processing here:
            print(event)

def main():
    """Entry point: example to use FritzMonitor.
    """
    try:
        # as a context manager FritzMonitor will shut down the monitor thread
        with FritzMonitor(address='192.168.178.1') as monitor:
            event_queue = monitor.start()
            process_events(monitor, event_queue)
    except (OSError, KeyboardInterrupt) as err:
        print(err)

if __name__ == "__main__":
    main()
