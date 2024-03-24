# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtDBus, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtDBus`

import PySide6.QtDBus
import PySide6.QtCore

import enum
from typing import Any, ClassVar, Dict, List, Optional, Sequence, Type, Union, overload
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


NoneType = type(None)


class QDBus(Shiboken.Object):

    class CallMode(enum.Enum):

        NoBlock                  : QDBus.CallMode = ... # 0x0
        Block                    : QDBus.CallMode = ... # 0x1
        BlockWithGui             : QDBus.CallMode = ... # 0x2
        AutoDetect               : QDBus.CallMode = ... # 0x3


class QDBusAbstractAdaptor(PySide6.QtCore.QObject):

    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def autoRelaySignals(self) -> bool: ...
    def setAutoRelaySignals(self, enable: bool) -> None: ...


class QDBusAbstractInterface(PySide6.QtDBus.QDBusAbstractInterfaceBase):

    def __init__(self, service: str, path: str, interface: bytes, connection: PySide6.QtDBus.QDBusConnection, parent: PySide6.QtCore.QObject) -> None: ...

    def asyncCall(self, method: str) -> PySide6.QtDBus.QDBusPendingCall: ...
    def asyncCallWithArgumentList(self, method: str, args: Sequence[Any]) -> PySide6.QtDBus.QDBusPendingCall: ...
    @overload
    def call(self, arg__1: PySide6.QtDBus.QDBus.CallMode, arg__2: str, arg__3: Any) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def call(self, arg__1: PySide6.QtDBus.QDBus.CallMode, arg__2: str, arg__3: Any, arg__4: Any) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def call(self, arg__1: PySide6.QtDBus.QDBus.CallMode, arg__2: str, arg__3: Any, arg__4: Any, arg__5: Any) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def call(self, arg__1: PySide6.QtDBus.QDBus.CallMode, arg__2: str, arg__3: Any, arg__4: Any, arg__5: Any, arg__6: Any) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def call(self, arg__1: PySide6.QtDBus.QDBus.CallMode, arg__2: str, arg__3: Any, arg__4: Any, arg__5: Any, arg__6: Any, arg__7: Any) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def call(self, arg__1: PySide6.QtDBus.QDBus.CallMode, arg__2: str, arg__3: Any, arg__4: Any, arg__5: Any, arg__6: Any, arg__7: Any, arg__8: Any) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def call(self, arg__1: PySide6.QtDBus.QDBus.CallMode, arg__2: str, arg__3: Any, arg__4: Any, arg__5: Any, arg__6: Any, arg__7: Any, arg__8: Any, arg__9: Any) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def call(self, arg__1: PySide6.QtDBus.QDBus.CallMode, arg__2: str, arg__3: Any, arg__4: Any, arg__5: Any, arg__6: Any, arg__7: Any, arg__8: Any, arg__9: Any, arg__10: Any) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def call(self, arg__1: str, arg__2: Any) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def call(self, arg__1: str, arg__2: Any, arg__3: Any) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def call(self, arg__1: str, arg__2: Any, arg__3: Any, arg__4: Any) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def call(self, arg__1: str, arg__2: Any, arg__3: Any, arg__4: Any, arg__5: Any) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def call(self, method: str) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def call(self, mode: PySide6.QtDBus.QDBus.CallMode, method: str) -> PySide6.QtDBus.QDBusMessage: ...
    def callWithArgumentList(self, mode: PySide6.QtDBus.QDBus.CallMode, method: str, args: Sequence[Any]) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def callWithCallback(self, method: str, args: Sequence[Any], receiver: PySide6.QtCore.QObject, member: bytes) -> bool: ...
    @overload
    def callWithCallback(self, method: str, args: Sequence[Any], receiver: PySide6.QtCore.QObject, member: bytes, errorSlot: bytes) -> bool: ...
    def connectNotify(self, signal: PySide6.QtCore.QMetaMethod) -> None: ...
    def connection(self) -> PySide6.QtDBus.QDBusConnection: ...
    def disconnectNotify(self, signal: PySide6.QtCore.QMetaMethod) -> None: ...
    def interface(self) -> str: ...
    def internalConstCall(self, mode: PySide6.QtDBus.QDBus.CallMode, method: str, args: Sequence[Any] = ...) -> PySide6.QtDBus.QDBusMessage: ...
    def internalPropGet(self, propname: bytes) -> Any: ...
    def internalPropSet(self, propname: bytes, value: Any) -> None: ...
    def isValid(self) -> bool: ...
    def lastError(self) -> PySide6.QtDBus.QDBusError: ...
    def path(self) -> str: ...
    def service(self) -> str: ...
    def setTimeout(self, timeout: int) -> None: ...
    def timeout(self) -> int: ...


class QDBusAbstractInterfaceBase(PySide6.QtCore.QObject):

    destroyed                : ClassVar[Signal] = ... # destroyed()
    objectNameChanged        : ClassVar[Signal] = ... # objectNameChanged(QString)


class QDBusArgument(Shiboken.Object):

    class ElementType(enum.Enum):

        UnknownType              : QDBusArgument.ElementType = ... # -0x1
        BasicType                : QDBusArgument.ElementType = ... # 0x0
        VariantType              : QDBusArgument.ElementType = ... # 0x1
        ArrayType                : QDBusArgument.ElementType = ... # 0x2
        StructureType            : QDBusArgument.ElementType = ... # 0x3
        MapType                  : QDBusArgument.ElementType = ... # 0x4
        MapEntryType             : QDBusArgument.ElementType = ... # 0x5


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtDBus.QDBusArgument) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    @overload
    def __lshift__(self, arg: PySide6.QtDBus.QDBusObjectPath) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, arg: PySide6.QtDBus.QDBusSignature) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, arg: PySide6.QtDBus.QDBusUnixFileDescriptor) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, arg: PySide6.QtDBus.QDBusVariant) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, arg: str) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, arg: Sequence[str]) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, arg: bool) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, arg: float) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, arg: int) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, arg: int) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, arg: int) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, arg: int) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, arg: Union[PySide6.QtCore.QByteArray, bytes]) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, arg: int) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, arg: int) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, arg: int) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, date: PySide6.QtCore.QDate) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, dt: PySide6.QtCore.QDateTime) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, line: PySide6.QtCore.QLine) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, line: Union[PySide6.QtCore.QLineF, PySide6.QtCore.QLine]) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, list: Sequence[Any]) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, map: Dict[str, Any]) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, map: Dict[str, Any]) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, pt: PySide6.QtCore.QPoint) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, pt: Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint]) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, rect: PySide6.QtCore.QRect) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, rect: Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, size: PySide6.QtCore.QSize) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, size: Union[PySide6.QtCore.QSizeF, PySide6.QtCore.QSize]) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __lshift__(self, time: PySide6.QtCore.QTime) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, arg: PySide6.QtDBus.QDBusObjectPath) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, arg: PySide6.QtDBus.QDBusSignature) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, arg: PySide6.QtDBus.QDBusUnixFileDescriptor) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, arg: PySide6.QtDBus.QDBusVariant) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, arg: str) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, arg: Sequence[str]) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, arg: bool) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, arg: float) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, arg: int) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, arg: int) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, arg: int) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, arg: int) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, arg: Union[PySide6.QtCore.QByteArray, bytes]) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, arg: int) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, arg: int) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, arg: int) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, date: PySide6.QtCore.QDate) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, dt: PySide6.QtCore.QDateTime) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, line: PySide6.QtCore.QLine) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, line: Union[PySide6.QtCore.QLineF, PySide6.QtCore.QLine]) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, pt: PySide6.QtCore.QPoint) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, pt: Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint]) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, rect: PySide6.QtCore.QRect) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, rect: Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, size: PySide6.QtCore.QSize) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, size: Union[PySide6.QtCore.QSizeF, PySide6.QtCore.QSize]) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, time: PySide6.QtCore.QTime) -> PySide6.QtDBus.QDBusArgument: ...
    @overload
    def __rshift__(self, v: Any) -> PySide6.QtDBus.QDBusArgument: ...
    def appendVariant(self, v: Any) -> None: ...
    def asVariant(self) -> Any: ...
    def atEnd(self) -> bool: ...
    @overload
    def beginArray(self) -> None: ...
    @overload
    def beginArray(self, elementMetaType: Union[PySide6.QtCore.QMetaType, PySide6.QtCore.QMetaType.Type]) -> None: ...
    @overload
    def beginArray(self, elementMetaTypeId: int) -> None: ...
    @overload
    def beginMap(self) -> None: ...
    @overload
    def beginMap(self, keyMetaType: Union[PySide6.QtCore.QMetaType, PySide6.QtCore.QMetaType.Type], valueMetaType: Union[PySide6.QtCore.QMetaType, PySide6.QtCore.QMetaType.Type]) -> None: ...
    @overload
    def beginMap(self, keyMetaTypeId: int, valueMetaTypeId: int) -> None: ...
    def beginMapEntry(self) -> None: ...
    def beginStructure(self) -> None: ...
    def currentSignature(self) -> str: ...
    def currentType(self) -> PySide6.QtDBus.QDBusArgument.ElementType: ...
    def endArray(self) -> None: ...
    def endMap(self) -> None: ...
    def endMapEntry(self) -> None: ...
    def endStructure(self) -> None: ...
    def swap(self, other: PySide6.QtDBus.QDBusArgument) -> None: ...


class QDBusConnection(Shiboken.Object):

    class BusType(enum.Enum):

        SessionBus               : QDBusConnection.BusType = ... # 0x0
        SystemBus                : QDBusConnection.BusType = ... # 0x1
        ActivationBus            : QDBusConnection.BusType = ... # 0x2


    class ConnectionCapability(enum.Flag):

        UnixFileDescriptorPassing: QDBusConnection.ConnectionCapability = ... # 0x1


    class RegisterOption(enum.Flag):

        ExportAdaptors           : QDBusConnection.RegisterOption = ... # 0x1
        ExportScriptableSlots    : QDBusConnection.RegisterOption = ... # 0x10
        ExportScriptableSignals  : QDBusConnection.RegisterOption = ... # 0x20
        ExportScriptableProperties: QDBusConnection.RegisterOption = ... # 0x40
        ExportScriptableInvokables: QDBusConnection.RegisterOption = ... # 0x80
        ExportScriptableContents : QDBusConnection.RegisterOption = ... # 0xf0
        ExportNonScriptableSlots : QDBusConnection.RegisterOption = ... # 0x100
        ExportAllSlots           : QDBusConnection.RegisterOption = ... # 0x110
        ExportNonScriptableSignals: QDBusConnection.RegisterOption = ... # 0x200
        ExportAllSignal          : QDBusConnection.RegisterOption = ... # 0x220
        ExportAllSignals         : QDBusConnection.RegisterOption = ... # 0x220
        ExportNonScriptableProperties: QDBusConnection.RegisterOption = ... # 0x400
        ExportAllProperties      : QDBusConnection.RegisterOption = ... # 0x440
        ExportNonScriptableInvokables: QDBusConnection.RegisterOption = ... # 0x800
        ExportAllInvokables      : QDBusConnection.RegisterOption = ... # 0x880
        ExportNonScriptableContents: QDBusConnection.RegisterOption = ... # 0xf00
        ExportAllContents        : QDBusConnection.RegisterOption = ... # 0xff0
        ExportChildObjects       : QDBusConnection.RegisterOption = ... # 0x1000


    class UnregisterMode(enum.Enum):

        UnregisterNode           : QDBusConnection.UnregisterMode = ... # 0x0
        UnregisterTree           : QDBusConnection.UnregisterMode = ... # 0x1


    class VirtualObjectRegisterOption(enum.Flag):

        SingleNode               : QDBusConnection.VirtualObjectRegisterOption = ... # 0x0
        SubPath                  : QDBusConnection.VirtualObjectRegisterOption = ... # 0x1


    @overload
    def __init__(self, name: str) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtDBus.QDBusConnection) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def asyncCall(self, message: PySide6.QtDBus.QDBusMessage, timeout: int = ...) -> PySide6.QtDBus.QDBusPendingCall: ...
    def baseService(self) -> str: ...
    def call(self, message: PySide6.QtDBus.QDBusMessage, mode: PySide6.QtDBus.QDBus.CallMode = ..., timeout: int = ...) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def callWithCallback(self, message: PySide6.QtDBus.QDBusMessage, receiver: PySide6.QtCore.QObject, returnMethod: bytes, errorMethod: bytes, timeout: int = ...) -> bool: ...
    @overload
    def callWithCallback(self, message: PySide6.QtDBus.QDBusMessage, receiver: PySide6.QtCore.QObject, slot: bytes, timeout: int = ...) -> bool: ...
    @overload
    def connect(self, service: str, path: str, interface: str, name: str, argumentMatch: Sequence[str], signature: str, receiver: PySide6.QtCore.QObject, slot: bytes) -> bool: ...
    @overload
    def connect(self, service: str, path: str, interface: str, name: str, receiver: PySide6.QtCore.QObject, slot: bytes) -> bool: ...
    @overload
    def connect(self, service: str, path: str, interface: str, name: str, signature: str, receiver: PySide6.QtCore.QObject, slot: bytes) -> bool: ...
    @overload
    @staticmethod
    def connectToBus(address: str, name: str) -> PySide6.QtDBus.QDBusConnection: ...
    @overload
    @staticmethod
    def connectToBus(type: PySide6.QtDBus.QDBusConnection.BusType, name: str) -> PySide6.QtDBus.QDBusConnection: ...
    @staticmethod
    def connectToPeer(address: str, name: str) -> PySide6.QtDBus.QDBusConnection: ...
    def connectionCapabilities(self) -> PySide6.QtDBus.QDBusConnection.ConnectionCapability: ...
    @overload
    def disconnect(self, service: str, path: str, interface: str, name: str, argumentMatch: Sequence[str], signature: str, receiver: PySide6.QtCore.QObject, slot: bytes) -> bool: ...
    @overload
    def disconnect(self, service: str, path: str, interface: str, name: str, receiver: PySide6.QtCore.QObject, slot: bytes) -> bool: ...
    @overload
    def disconnect(self, service: str, path: str, interface: str, name: str, signature: str, receiver: PySide6.QtCore.QObject, slot: bytes) -> bool: ...
    @staticmethod
    def disconnectFromBus(name: str) -> None: ...
    @staticmethod
    def disconnectFromPeer(name: str) -> None: ...
    def interface(self) -> PySide6.QtDBus.QDBusConnectionInterface: ...
    def internalPointer(self) -> int: ...
    def isConnected(self) -> bool: ...
    def lastError(self) -> PySide6.QtDBus.QDBusError: ...
    @staticmethod
    def localMachineId() -> PySide6.QtCore.QByteArray: ...
    def name(self) -> str: ...
    def objectRegisteredAt(self, path: str) -> PySide6.QtCore.QObject: ...
    @overload
    def registerObject(self, path: str, interface: str, object: PySide6.QtCore.QObject, options: PySide6.QtDBus.QDBusConnection.RegisterOption = ...) -> bool: ...
    @overload
    def registerObject(self, path: str, object: PySide6.QtCore.QObject, options: PySide6.QtDBus.QDBusConnection.RegisterOption = ...) -> bool: ...
    def registerService(self, serviceName: str) -> bool: ...
    def registerVirtualObject(self, path: str, object: PySide6.QtDBus.QDBusVirtualObject, options: PySide6.QtDBus.QDBusConnection.VirtualObjectRegisterOption = ...) -> bool: ...
    def send(self, message: PySide6.QtDBus.QDBusMessage) -> bool: ...
    @staticmethod
    def sessionBus() -> PySide6.QtDBus.QDBusConnection: ...
    def swap(self, other: PySide6.QtDBus.QDBusConnection) -> None: ...
    @staticmethod
    def systemBus() -> PySide6.QtDBus.QDBusConnection: ...
    def unregisterObject(self, path: str, mode: PySide6.QtDBus.QDBusConnection.UnregisterMode = ...) -> None: ...
    def unregisterService(self, serviceName: str) -> bool: ...


class QDBusConnectionInterface(PySide6.QtDBus.QDBusAbstractInterface):

    NameAcquired             : ClassVar[Signal] = ... # NameAcquired(QString)
    NameLost                 : ClassVar[Signal] = ... # NameLost(QString)
    NameOwnerChanged         : ClassVar[Signal] = ... # NameOwnerChanged(QString,QString,QString)
    callWithCallbackFailed   : ClassVar[Signal] = ... # callWithCallbackFailed(QDBusError,QDBusMessage)
    serviceOwnerChanged      : ClassVar[Signal] = ... # serviceOwnerChanged(QString,QString,QString)
    serviceRegistered        : ClassVar[Signal] = ... # serviceRegistered(QString)
    serviceUnregistered      : ClassVar[Signal] = ... # serviceUnregistered(QString)

    class RegisterServiceReply(enum.Enum):

        ServiceNotRegistered     : QDBusConnectionInterface.RegisterServiceReply = ... # 0x0
        ServiceRegistered        : QDBusConnectionInterface.RegisterServiceReply = ... # 0x1
        ServiceQueued            : QDBusConnectionInterface.RegisterServiceReply = ... # 0x2


    class ServiceQueueOptions(enum.Enum):

        DontQueueService         : QDBusConnectionInterface.ServiceQueueOptions = ... # 0x0
        QueueService             : QDBusConnectionInterface.ServiceQueueOptions = ... # 0x1
        ReplaceExistingService   : QDBusConnectionInterface.ServiceQueueOptions = ... # 0x2


    class ServiceReplacementOptions(enum.Enum):

        DontAllowReplacement     : QDBusConnectionInterface.ServiceReplacementOptions = ... # 0x0
        AllowReplacement         : QDBusConnectionInterface.ServiceReplacementOptions = ... # 0x1


    def activatableServiceNames(self) -> PySide6.QtDBus.QDBusReply: ...
    def connectNotify(self, arg__1: PySide6.QtCore.QMetaMethod) -> None: ...
    def disconnectNotify(self, arg__1: PySide6.QtCore.QMetaMethod) -> None: ...
    def isServiceRegistered(self, arg__1: str) -> PySide6.QtDBus.QDBusReply: ...
    def registerService(self, arg__1: str, arg__2: PySide6.QtDBus.QDBusConnectionInterface.ServiceQueueOptions, arg__3: PySide6.QtDBus.QDBusConnectionInterface.ServiceReplacementOptions) -> PySide6.QtDBus.QDBusReply: ...
    def registeredServiceNames(self) -> PySide6.QtDBus.QDBusReply: ...
    def serviceOwner(self, arg__1: str) -> PySide6.QtDBus.QDBusReply: ...
    def servicePid(self, arg__1: str) -> PySide6.QtDBus.QDBusReply: ...
    def serviceUid(self, arg__1: str) -> PySide6.QtDBus.QDBusReply: ...
    def startService(self, arg__1: str) -> PySide6.QtDBus.QDBusReply: ...
    def unregisterService(self, arg__1: str) -> PySide6.QtDBus.QDBusReply: ...


class QDBusContext(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, QDBusContext: PySide6.QtDBus.QDBusContext) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def calledFromDBus(self) -> bool: ...
    def connection(self) -> PySide6.QtDBus.QDBusConnection: ...
    def isDelayedReply(self) -> bool: ...
    def message(self) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def sendErrorReply(self, name: str, msg: str = ...) -> None: ...
    @overload
    def sendErrorReply(self, type: PySide6.QtDBus.QDBusError.ErrorType, msg: str = ...) -> None: ...
    def setDelayedReply(self, enable: bool) -> None: ...


class QDBusError(Shiboken.Object):

    class ErrorType(enum.Enum):

        NoError                  : QDBusError.ErrorType = ... # 0x0
        Other                    : QDBusError.ErrorType = ... # 0x1
        Failed                   : QDBusError.ErrorType = ... # 0x2
        NoMemory                 : QDBusError.ErrorType = ... # 0x3
        ServiceUnknown           : QDBusError.ErrorType = ... # 0x4
        NoReply                  : QDBusError.ErrorType = ... # 0x5
        BadAddress               : QDBusError.ErrorType = ... # 0x6
        NotSupported             : QDBusError.ErrorType = ... # 0x7
        LimitsExceeded           : QDBusError.ErrorType = ... # 0x8
        AccessDenied             : QDBusError.ErrorType = ... # 0x9
        NoServer                 : QDBusError.ErrorType = ... # 0xa
        Timeout                  : QDBusError.ErrorType = ... # 0xb
        NoNetwork                : QDBusError.ErrorType = ... # 0xc
        AddressInUse             : QDBusError.ErrorType = ... # 0xd
        Disconnected             : QDBusError.ErrorType = ... # 0xe
        InvalidArgs              : QDBusError.ErrorType = ... # 0xf
        UnknownMethod            : QDBusError.ErrorType = ... # 0x10
        TimedOut                 : QDBusError.ErrorType = ... # 0x11
        InvalidSignature         : QDBusError.ErrorType = ... # 0x12
        UnknownInterface         : QDBusError.ErrorType = ... # 0x13
        UnknownObject            : QDBusError.ErrorType = ... # 0x14
        UnknownProperty          : QDBusError.ErrorType = ... # 0x15
        PropertyReadOnly         : QDBusError.ErrorType = ... # 0x16
        InternalError            : QDBusError.ErrorType = ... # 0x17
        InvalidService           : QDBusError.ErrorType = ... # 0x18
        InvalidObjectPath        : QDBusError.ErrorType = ... # 0x19
        InvalidInterface         : QDBusError.ErrorType = ... # 0x1a
        InvalidMember            : QDBusError.ErrorType = ... # 0x1b
        LastErrorType            : QDBusError.ErrorType = ... # 0x1b


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, error: PySide6.QtDBus.QDBusError.ErrorType, message: str) -> None: ...
    @overload
    def __init__(self, msg: PySide6.QtDBus.QDBusMessage) -> None: ...
    @overload
    def __init__(self, other: Union[PySide6.QtDBus.QDBusError, PySide6.QtDBus.QDBusMessage]) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    @staticmethod
    def errorString(error: PySide6.QtDBus.QDBusError.ErrorType) -> str: ...
    def isValid(self) -> bool: ...
    def message(self) -> str: ...
    def name(self) -> str: ...
    def swap(self, other: Union[PySide6.QtDBus.QDBusError, PySide6.QtDBus.QDBusMessage]) -> None: ...
    def type(self) -> PySide6.QtDBus.QDBusError.ErrorType: ...


class QDBusInterface(PySide6.QtDBus.QDBusAbstractInterface):

    def __init__(self, service: str, path: str, interface: str = ..., connection: PySide6.QtDBus.QDBusConnection = ..., parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...


class QDBusMessage(Shiboken.Object):

    class MessageType(enum.Enum):

        InvalidMessage           : QDBusMessage.MessageType = ... # 0x0
        MethodCallMessage        : QDBusMessage.MessageType = ... # 0x1
        ReplyMessage             : QDBusMessage.MessageType = ... # 0x2
        ErrorMessage             : QDBusMessage.MessageType = ... # 0x3
        SignalMessage            : QDBusMessage.MessageType = ... # 0x4


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtDBus.QDBusMessage) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(self, arg: Any) -> PySide6.QtDBus.QDBusMessage: ...
    def arguments(self) -> List[Any]: ...
    def autoStartService(self) -> bool: ...
    @overload
    @staticmethod
    def createError(err: Union[PySide6.QtDBus.QDBusError, PySide6.QtDBus.QDBusMessage]) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    @staticmethod
    def createError(name: str, msg: str) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    @staticmethod
    def createError(type: PySide6.QtDBus.QDBusError.ErrorType, msg: str) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def createErrorReply(self, err: Union[PySide6.QtDBus.QDBusError, PySide6.QtDBus.QDBusMessage]) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def createErrorReply(self, name: str, msg: str) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def createErrorReply(self, type: PySide6.QtDBus.QDBusError.ErrorType, msg: str) -> PySide6.QtDBus.QDBusMessage: ...
    @staticmethod
    def createMethodCall(destination: str, path: str, interface: str, method: str) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def createReply(self, argument: Any) -> PySide6.QtDBus.QDBusMessage: ...
    @overload
    def createReply(self, arguments: Sequence[Any] = ...) -> PySide6.QtDBus.QDBusMessage: ...
    @staticmethod
    def createSignal(path: str, interface: str, name: str) -> PySide6.QtDBus.QDBusMessage: ...
    @staticmethod
    def createTargetedSignal(service: str, path: str, interface: str, name: str) -> PySide6.QtDBus.QDBusMessage: ...
    def errorMessage(self) -> str: ...
    def errorName(self) -> str: ...
    def interface(self) -> str: ...
    def isDelayedReply(self) -> bool: ...
    def isInteractiveAuthorizationAllowed(self) -> bool: ...
    def isReplyRequired(self) -> bool: ...
    def member(self) -> str: ...
    def path(self) -> str: ...
    def service(self) -> str: ...
    def setArguments(self, arguments: Sequence[Any]) -> None: ...
    def setAutoStartService(self, enable: bool) -> None: ...
    def setDelayedReply(self, enable: bool) -> None: ...
    def setInteractiveAuthorizationAllowed(self, enable: bool) -> None: ...
    def signature(self) -> str: ...
    def swap(self, other: PySide6.QtDBus.QDBusMessage) -> None: ...
    def type(self) -> PySide6.QtDBus.QDBusMessage.MessageType: ...


class QDBusObjectPath(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, path: str) -> None: ...
    @overload
    def __init__(self, path: bytes) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def path(self) -> str: ...
    def setPath(self, path: str) -> None: ...
    def swap(self, other: PySide6.QtDBus.QDBusObjectPath) -> None: ...


class QDBusPendingCall(Shiboken.Object):

    def __init__(self, other: PySide6.QtDBus.QDBusPendingCall) -> None: ...

    def error(self) -> PySide6.QtDBus.QDBusError: ...
    @staticmethod
    def fromCompletedCall(message: PySide6.QtDBus.QDBusMessage) -> PySide6.QtDBus.QDBusPendingCall: ...
    @staticmethod
    def fromError(error: Union[PySide6.QtDBus.QDBusError, PySide6.QtDBus.QDBusMessage]) -> PySide6.QtDBus.QDBusPendingCall: ...
    def isError(self) -> bool: ...
    def isFinished(self) -> bool: ...
    def isValid(self) -> bool: ...
    def reply(self) -> PySide6.QtDBus.QDBusMessage: ...
    def swap(self, other: PySide6.QtDBus.QDBusPendingCall) -> None: ...
    def waitForFinished(self) -> None: ...


class QDBusPendingCallWatcher(PySide6.QtCore.QObject, PySide6.QtDBus.QDBusPendingCall):

    finished                 : ClassVar[Signal] = ... # finished()

    def __init__(self, call: PySide6.QtDBus.QDBusPendingCall, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def waitForFinished(self) -> None: ...


class QDBusReply(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, reply: PySide6.QtDBus.QDBusMessage) -> None: ...

    def error(self) -> PySide6.QtDBus.QDBusError: ...
    def isValid(self) -> bool: ...
    def value(self) -> Any: ...


class QDBusServer(PySide6.QtCore.QObject):

    newConnection            : ClassVar[Signal] = ... # newConnection(QDBusConnection)

    @overload
    def __init__(self, address: str, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def address(self) -> str: ...
    def isAnonymousAuthenticationAllowed(self) -> bool: ...
    def isConnected(self) -> bool: ...
    def lastError(self) -> PySide6.QtDBus.QDBusError: ...
    def setAnonymousAuthenticationAllowed(self, value: bool) -> None: ...


class QDBusServiceWatcher(PySide6.QtCore.QObject):

    serviceOwnerChanged      : ClassVar[Signal] = ... # serviceOwnerChanged(QString,QString,QString)
    serviceRegistered        : ClassVar[Signal] = ... # serviceRegistered(QString)
    serviceUnregistered      : ClassVar[Signal] = ... # serviceUnregistered(QString)

    class WatchModeFlag(enum.Flag):

        WatchForRegistration     : QDBusServiceWatcher.WatchModeFlag = ... # 0x1
        WatchForUnregistration   : QDBusServiceWatcher.WatchModeFlag = ... # 0x2
        WatchForOwnerChange      : QDBusServiceWatcher.WatchModeFlag = ... # 0x3


    @overload
    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, service: str, connection: PySide6.QtDBus.QDBusConnection, watchMode: PySide6.QtDBus.QDBusServiceWatcher.WatchModeFlag = ..., parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def addWatchedService(self, newService: str) -> None: ...
    def connection(self) -> PySide6.QtDBus.QDBusConnection: ...
    def removeWatchedService(self, service: str) -> bool: ...
    def setConnection(self, connection: PySide6.QtDBus.QDBusConnection) -> None: ...
    def setWatchMode(self, mode: PySide6.QtDBus.QDBusServiceWatcher.WatchModeFlag) -> None: ...
    def setWatchedServices(self, services: Sequence[str]) -> None: ...
    def watchMode(self) -> PySide6.QtDBus.QDBusServiceWatcher.WatchModeFlag: ...
    def watchedServices(self) -> List[str]: ...


class QDBusSignature(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, signature: str) -> None: ...
    @overload
    def __init__(self, signature: bytes) -> None: ...

    def setSignature(self, signature: str) -> None: ...
    def signature(self) -> str: ...
    def swap(self, other: PySide6.QtDBus.QDBusSignature) -> None: ...


class QDBusUnixFileDescriptor(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, fileDescriptor: int) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtDBus.QDBusUnixFileDescriptor) -> None: ...

    def fileDescriptor(self) -> int: ...
    def giveFileDescriptor(self, fileDescriptor: int) -> None: ...
    @staticmethod
    def isSupported() -> bool: ...
    def isValid(self) -> bool: ...
    def setFileDescriptor(self, fileDescriptor: int) -> None: ...
    def swap(self, other: PySide6.QtDBus.QDBusUnixFileDescriptor) -> None: ...
    def takeFileDescriptor(self) -> int: ...


class QDBusVariant(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, variant: Any) -> None: ...

    def setVariant(self, variant: Any) -> None: ...
    def swap(self, other: PySide6.QtDBus.QDBusVariant) -> None: ...
    def variant(self) -> Any: ...


class QDBusVirtualObject(PySide6.QtCore.QObject):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def handleMessage(self, message: PySide6.QtDBus.QDBusMessage, connection: PySide6.QtDBus.QDBusConnection) -> bool: ...
    def introspect(self, path: str) -> str: ...


class QIntList(object): ...


# eof
