import logging
import time
from config.logging_config import configure_logging
from src.networking.can_system import CANSystem


def main() -> None:
    """Start CAN-Sentinel and demonstrate CAN attack detection."""
    configure_logging()
    logger = logging.getLogger(__name__)

    logger.info("===== CAN-Sentinel =====")
    logger.info("Starting CAN monitoring system...")

    system = CANSystem()
    system.start()

    try:
        logger.info("Normal CAN traffic is running.")
        time.sleep(5)

        logger.warning("===== STARTING FAKE SPEED ATTACK =====")
        system.start_fake_speed_attack()
        time.sleep(5)

        logger.warning("===== STOPPING FAKE SPEED ATTACK =====")
        system.stop_fake_speed_attack()
        time.sleep(3)

    except KeyboardInterrupt:
        logger.info("Shutdown requested by user.")
    finally:
        system.stop()
        logger.info("CAN-Sentinel stopped.")


if __name__ == "__main__":
    main()
