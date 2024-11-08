import win32serviceutil # Библеотека для управления службами (установка, запуск и остановка)
import win32service # Библеотека для работы с интерфейсом служб
import win32event # Библеотека для создания событий
import servicemanager # Библеотека для логирования в журнал событий

# Класс службы который наследует билеотеку для создания службы
class EmptyWinService(win32serviceutil.ServiceFramework):
    _svc_name_ = "EmptyService"
    _svc_display_name_ = "My Empty Service"
    _svc_description_ = "This is a empty service."

	
    def __init__(self, args): # Конструтеор класса, который принимает значаения для создания службы
        win32serviceutil.ServiceFramework.__init__(self, args) # Инициализирует базовый класс службы.
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None) # Эта строчка служит флагом, чтобы служба могла ожидать сигнала завершения работы
        self.is_running = True

    def SvcStop(self): # Метод для остановки службы 
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING) # Строка для установки статуса "служба в процессе остановки"
        win32event.SetEvent(self.hWaitStop) # 
        self.is_running = False

    def SvcDoRun(self): # Основной метод службы, выполняющийся при запуске
        servicemanager.LogMsg( # Записывает сообщение в журнал событий, что служба запущена или то что остановлена
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, "")
        )
        while self.is_running: # Цикл с основной логикой службы
            win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE) # Строка которая ждет сигнал завершения службы
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STOPPED,
            (self._svc_name_, "")
        )
	
if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(EmptyWinService) # Строка для взаиможействия со службой через CLI 	