from datetime import datetime, timedelta

class Device:
    def __init__(self, device_id, device_type, owner, firmware_version='1.0.0'):
        self.device_id = device_id
        self.device_type = device_type
        self.firmware_version = firmware_version
        self.compliance_status = 'unknown'
        self.owner = owner
        self.last_security_scan = None
        self.is_active = True
        self.access_log = []

    def authorise_access(self, user):
        if not self.is_active:
            self.log_access(user.get_username(), 'Denied - Device inactive')
            return False
        if self.compliance_status != 'compliant' and not user.check_privileges('admin'):
            self.log_access(user.get_username(), 'Denied - Non-compliant device')
            return False
        if self.owner != user.get_username() and not user.check_privileges('admin'):
            self.log_access(user.get_username(), 'Denied - Not owner')
            return False
        self.log_access(user.get_username(), 'Access granted')
        return True

    def run_security_scan(self):
        self.last_security_scan = datetime.now()
        self.compliance_status = 'compliant'
        self.log_access('SYSTEM', 'Security scan completed')

    def check_compliance(self):
        if self.last_security_scan is None:
            self.compliance_status = 'unknown'
            return False
        if (datetime.now() - self.last_security_scan).days > 30:
            self.compliance_status = 'non-compliant'
            return False
        return self.compliance_status == 'compliant'

    def update_firmware(self, version, user):
        if not user.check_privileges('admin'):
            return False
        self.firmware_version = version
        self.log_access(user.get_username(), f'Firmware updated to {version}')
        return True

    def quarantine(self, user):
        if not user.check_privileges('admin'):
            return False
        self.is_active = False
        self.log_access(user.get_username(), 'Device quarantined')
        return True

    def log_access(self, username, action):
        self.access_log.append(f"{datetime.now()}: {username} - {action}")

    def get_info(self):
        return {
            'device_id': self.device_id,
            'device_type': self.device_type,
            'firmware_version': self.firmware_version,
            'compliance_status': self.compliance_status,
            'owner': self.owner,
            'is_active': self.is_active
        }


class DeviceManager:
    def __init__(self):
        self.devices = {}

    def add_device(self, device):
        self.devices[device.device_id] = device

    def remove_device(self, device_id, user):
        if not user.check_privileges('admin'):
            return False
        if device_id in self.devices:
            del self.devices[device_id]
            return True
        return False

    def generate_security_report(self, user):
        if not user.check_privileges('admin'):
            return None
        report = []
        for device in self.devices.values():
            device.check_compliance()
            report.append(device.get_info())
        return report