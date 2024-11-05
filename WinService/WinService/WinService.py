import win32serviceutil
import win32event
import servicemanager

class MyService(win32serviceutil.ServiceFramework):
	_svc_name_ = 'KennySrv'
	_svc_display_name_ = 'Kenny Test Service'
	_svc_description_ = 'Test Kenny Service'

	def __init__(self, args):
		win32serviceutil.ServiceFramework.__init__(self, args)
		self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
	
	def SvcDoRun(self):
		self.ReportServiceStatus(win32serviceutil.SERVICE_START_PENDING) 
		self.ReportServiceStatus(win32serviceutil.SERVICE_RUNNING)
		...
		win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)
	
	def SvcStop(self):
		self.ReportServiceStatus(win32serviceutil.SERVICE_STOP_PENDING)
		...
		win32event.SetEvent(self.stop_event)
		self.ReportServiceStatus(win32serviceutil.SERVICE_STOPPED)

