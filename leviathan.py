#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""


███████╗██╗     ███████╗██╗   ██╗██╗ █████╗ ████████╗██╗  ██╗ █████╗ ███╗   ██╗
██╔════╝██║     ██╔════╝██║   ██║██║██╔══██╗╚══██╔══╝██║  ██║██╔══██╗████╗  ██║
█████╗  ██║     █████╗  ██║   ██║██║███████║   ██║   ███████║███████║██╔██╗ ██║
██╔══╝  ██║     ██╔══╝  ╚██╗ ██╔╝██║██╔══██║   ██║   ██╔══██║██╔══██║██║╚██╗██║
███████╗███████╗███████╗ ╚████╔╝ ██║██║  ██║   ██║   ██║  ██║██║  ██║██║ ╚████║
╚══════╝╚══════╝╚══════╝  ╚═══╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

[ V1.0 THE SINGULARITY ] [ SHAMIR: ACTIVE ] [ KERNEL: LOCKED ] [ GUI: INTEGRATED ]
"""


# KATMAN 0: SİSTEM HAZIRLIĞI @theval3x


import os
import sys
import time
import json
import hashlib
import base64
import platform
import random
import datetime
import subprocess
import shutil
import ctypes
import gc
import threading
import queue
import logging
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Optional, Dict, List, Tuple, Any, Union
from numba import jit, njit
import traceback
import mmap
from tkinter import messagebox


def load_security_shield():
    
    system = platform.system()
    
    
    if system == "Windows":
        lib_name = "watchdog.dll"
    elif system == "Linux":
        lib_name = "watchdog.so"
    else:
        print("[!] Desteklenmeyen işletim sistemi.")
        sys.exit(1)

    lib_path = os.path.join(os.getcwd(), lib_name)

    if not os.path.exists(lib_path):
        print(f"[!] Kritik hata: {lib_name} bulunamadı!")
        sys.exit(1)

    try:
       
        shield = ctypes.CDLL(lib_path)
        
        
        if not shield.check_security():
            print("\n" + "!"*40)
            print("!!! GÜVENLİK İHLALİ TESPİT EDİLDİ !!!")
            print("Analiz aracı veya debugger engellendi.")
            print("!"*40 + "\n")
            sys.exit(0)
            
        print(f"[*] {system} Güvenlik Kalkanı: AKTİF")
        
    except Exception as e:
        print(f"[!] Shield yükleme hatası: {e}")
        sys.exit(1)


load_security_shield()




gc.collect() 
gc.disable() 


sys.setrecursionlimit(5000)


try:
    from numba import config
    config.THREADING_LAYER = 'omp' 
except ImportError:
    pass



try:
    import tkinter as tk
    from tkinter import ttk, messagebox, filedialog, scrolledtext
    from tkinter.font import Font
except ImportError:
    print("[!] Tkinter kuruluyor...")
    if platform.system() == "Linux":
        subprocess.call(["sudo", "apt-get", "install", "python3-tk", "-y"])
    import tkinter as tk
    from tkinter import ttk, messagebox, filedialog, scrolledtext


try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
except ImportError:
    print("[*] Cryptography kuruluyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography"])
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# KATMAN 1: SABİTLER VE YAPILANDIRMA


VERSION = "1.0"
CODENAME = "THE SINGULARITY BASTION"
AUTHOR = "Valex"


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GRAY = '\033[90m'
    CYAN = '\033[96m'

GUI_COLORS = {
    'bg': '#0a0a0a',
    'fg': '#00ff00',
    'accent': '#00aaff',
    'error': '#ff0000',
    'success': '#00ff00',
    'warning': '#ffaa00',
    'panel': '#1a1a1a',
    'text': '#ffffff',
    'dark': '#000000'
}




THEMES = {
    'karanlık': {
        'bg': '#0a0a0a',
        'fg': '#00ff00',
        'accent': '#00aaff',
        'error': '#ff0000',
        'success': '#00ff00',
        'warning': '#ffaa00',
        'panel': '#1a1a1a',
        'text': '#ffffff',
        'dark': '#000000',
        'button': '#333333',
        'button_text': '#00ff00',
        'name': '🌑 KARANLIK'
    },
    'aydınlık': {
        'bg': '#f0f0f0',
        'fg': '#0066cc',
        'accent': '#ff6600',
        'error': '#cc0000',
        'success': '#00aa00',
        'warning': '#ffaa00',
        'panel': '#ffffff',
        'text': '#000000',
        'dark': '#e0e0e0',
        'button': '#dddddd',
        'button_text': '#000000',
        'name': '☀️ AYDINLIK'
    },
    'matrix': {
        'bg': '#000000',
        'fg': '#00ff00',
        'accent': '#00cc00',
        'error': '#00ff00',
        'success': '#00ff00',
        'warning': '#00ff00',
        'panel': '#0a0a0a',
        'text': '#00ff00',
        'dark': '#001100',
        'button': '#003300',
        'button_text': '#00ff00',
        'name': '💚 MATRİX'
    },
    'hacker': {
        'bg': '#0a0a0a',
        'fg': '#ff0000',
        'accent': '#ff3300',
        'error': '#ff0000',
        'success': '#ff0000',
        'warning': '#ff6600',
        'panel': '#1a0000',
        'text': '#ff5555',
        'dark': '#200000',
        'button': '#330000',
        'button_text': '#ff0000',
        'name': '🔥 HACKER'
    }
}


CURRENT_THEME = 'karanlık'
GUI_COLORS = THEMES[CURRENT_THEME]


# KATMAN 2: KERNEL & GHOST PROTECTION


class GhostProtection:
    """Sistem seviyesinde güvenlik önlemleri ve anti-forensic korumalar"""
    
    def __init__(self):
        self.os_name = platform.system()
        self.protection_active = False
        self._apply_protections()
    
    def _apply_protections(self):
        """Tüm korumaları uygula"""
        if self.os_name == "Linux":
            self._apply_linux_hardening()
        elif self.os_name == "Windows":
            self._apply_windows_shield()
        self.protection_active = True
    
    def _apply_linux_hardening(self):
        """Linux çekirdeği seviyesinde koruma"""
        try:
            libc = ctypes.CDLL("libc.so.6")
            
            
            libc.prctl(4, 0, 0, 0, 0)
            
            
            libc.mlockall(3)
            
            
            
            print(f"{Colors.BLUE}[!] LINUX KERNEL SHIELD: ACTIVE (Ptrace & Swap Blocked){Colors.END}")
        except Exception as e:
            print(f"{Colors.YELLOW}[!] KERNEL WARNING: {e}{Colors.END}")
    
    def _apply_windows_shield(self):
        """Windows koruma mekanizmaları"""
        try:
            
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            ctypes.windll.user32.SetWindowDisplayAffinity(hwnd, 0x11)
            
            
            
            print(f"{Colors.BLUE}[!] WINDOWS SHIELD: ANTI-CAPTURE ACTIVE{Colors.END}")
        except Exception as e:
            print(f"{Colors.YELLOW}[!] WINDOWS SHIELD ERROR: {e}{Colors.END}")
    
    def neural_jammer(self, stop_event: threading.Event):
        """Keylogger'lara karşı sinyal bozucu"""
        if self.os_name != "Windows":
            return
        
        try:
            while not stop_event.is_set():
                
                for _ in range(random.randint(1, 5)):
                    key = random.randint(0x41, 0x5A)
                    ctypes.windll.user32.keybd_event(key, 0, 0, 0)
                    time.sleep(random.uniform(0.001, 0.003))
                    ctypes.windll.user32.keybd_event(key, 0, 2, 0)
                
                
                time.sleep(random.uniform(0.01, 0.1))
        except:
            pass
    
    def secure_memory_wipe(self, *args):
        """Bellekteki verileri fiziksel olarak temizle"""
        for obj in args:
            try:
                if isinstance(obj, (bytes, bytearray)):
                    
                    if self.os_name == "Linux":
                        try:
                            libc = ctypes.CDLL("libc.so.6")
                            libc.mlock(id(obj), len(obj))
                        except:
                            pass
                    
                    
                    ctypes.memset(id(obj) + 20, 0, len(obj))
                    
                    
                    if self.os_name == "Linux":
                        try:
                            libc.munlock(id(obj), len(obj))
                        except:
                            pass
                
                elif isinstance(obj, str):
                    
                    obj = obj[:0]
                
                del obj
            except:
                pass
        
        gc.collect()
    
    def secure_delete(self, filepath: str, passes: int = 3):
        """Dosyayı güvenli şekilde sil (forensic analysis engelle)"""
        if not os.path.exists(filepath):
            return
        
        try:
            file_size = os.path.getsize(filepath)
            
            
            with open(filepath, "r+b") as f:
                for p in range(passes):
                    f.seek(0)
                    
                    if p == 0:
                        
                        f.write(b'\xFF' * file_size)
                    elif p == 1:
                       
                        f.write(os.urandom(file_size))
                    else:
                        
                        f.write(b'\x00' * file_size)
                    
                    f.flush()
                    os.fsync(f.fileno())
                    time.sleep(0.1)
            
            
            random_name = hashlib.sha3_256(os.urandom(32)).hexdigest()
            random_path = os.path.join(os.path.dirname(filepath), random_name)
            os.rename(filepath, random_path)
            
            # Sil
            os.remove(random_path)
            
        except Exception as e:
            
            try:
                os.remove(filepath)
            except:
                pass


# KATMAN 3: SHAMIR SECRET SHARING (GERÇEK IMPLEMENTASYON)


class ShamirSecretSharing:
    """
    Shamir'in Secret Sharing algoritmasının tam implementasyonu
    GF(256) üzerinde polinom interpolasyonu ile
    """
    
    
    GF_SIZE = 256
    PRIMITIVE = 0x11D  
    
    @staticmethod
    def _gf_add(x: int, y: int) -> int:
        """GF(256)'da toplama (XOR)"""
        return x ^ y
    
    @staticmethod
    def _gf_sub(x: int, y: int) -> int:
        """GF(256)'da çıkarma (XOR ile aynı)"""
        return x ^ y
    
    @staticmethod
    def _gf_mul(x: int, y: int) -> int:
        """GF(256)'da çarpma"""
        if x == 0 or y == 0:
            return 0
        
        result = 0
        while y:
            if y & 1:
                result ^= x
            x <<= 1
            if x & 0x100:
                x ^= ShamirSecretSharing.PRIMITIVE
            y >>= 1
        return result & 0xFF
    
    @staticmethod
    def _gf_div(x: int, y: int) -> int:
        """GF(256)'da bölme"""
        if y == 0:
            raise ZeroDivisionError("Division by zero in GF(256)")
        if x == 0:
            return 0
        return ShamirSecretSharing._gf_mul(x, ShamirSecretSharing._gf_inv(y))
    
    @staticmethod
    def _gf_pow(x: int, power: int) -> int:
        """GF(256)'da üs alma"""
        result = 1
        for _ in range(power):
            result = ShamirSecretSharing._gf_mul(result, x)
        return result
    
    @staticmethod
    def _gf_inv(x: int) -> int:
        """GF(256)'da ters eleman (x * inv(x) = 1)"""
        if x == 0:
            return 0
        
        
        for i in range(1, ShamirSecretSharing.GF_SIZE):
            if ShamirSecretSharing._gf_mul(x, i) == 1:
                return i
        return 0
    
    @staticmethod
    def _eval_poly(coeffs: List[int], x: int) -> int:
        """Polinom değerlendirme (Horner metodu)"""
        result = 0
        for coeff in reversed(coeffs):
            result = ShamirSecretSharing._gf_add(
                ShamirSecretSharing._gf_mul(result, x), coeff
            )
        return result
    
    @staticmethod
    def _interpolate(x_s: List[int], y_s: List[int], x: int) -> int:
        """Lagrange interpolasyonu"""
        n = len(x_s)
        result = 0
        
        for i in range(n):
            term = y_s[i]
            for j in range(n):
                if j != i:
                    numerator = ShamirSecretSharing._gf_sub(x, x_s[j])
                    denominator = ShamirSecretSharing._gf_sub(x_s[i], x_s[j])
                    term = ShamirSecretSharing._gf_mul(
                        term, 
                        ShamirSecretSharing._gf_div(numerator, denominator)
                    )
            result = ShamirSecretSharing._gf_add(result, term)
        
        return result
    
    @staticmethod
    def split(secret: bytes, threshold: int = 3, shares: int = 5) -> List[Tuple[int, bytes]]:
        """
        Secret'ı Shamir ile parçalara böl
        
        Args:
            secret: Gizli veri (bytes)
            threshold: Gereken minimum parça sayısı
            shares: Toplam parça sayısı
        
        Returns:
            List of (share_id, share_data) tuples
        """
        if threshold < 2:
            raise ValueError("Threshold must be at least 2")
        if shares < threshold:
            raise ValueError("Shares must be >= threshold")
        if not secret:
            raise ValueError("Secret cannot be empty")
        
        try:
            
            secret_bytes = list(secret)
            secret_len = len(secret_bytes)
            
            
            all_shares = [[] for _ in range(shares)]
            
            for byte_idx in range(secret_len):
                
                coeffs = [secret_bytes[byte_idx]]  
                for _ in range(threshold - 1):
                    coeffs.append(random.randint(1, 255))
                
               
                for share_idx in range(shares):
                    x = share_idx + 1  
                    y = ShamirSecretSharing._eval_poly(coeffs, x)
                    all_shares[share_idx].append(y)
            
            
            result = []
            for share_idx in range(shares):
                share_data = bytes(all_shares[share_idx])
                result.append((share_idx, share_data))
            
            return result
            
        except Exception as e:
            print(f"Shamir split error: {e}")
            return None
    
    @staticmethod
    def combine(shares: List[Tuple[int, bytes]]) -> Optional[bytes]:
        """
        Parçalardan secret'ı kurtar
        
        Args:
            shares: List of (share_id, share_data) tuples
        
        Returns:
            Recovered secret bytes or None if failed
        """
        if len(shares) < 2:
            raise ValueError("At least 2 shares required")
        
        try:
           
            x_vals = [s[0] + 1 for s in shares]  
            share_data = [list(s[1]) for s in shares]
            
            secret_len = len(share_data[0])
            recovered = []
            
            for byte_idx in range(secret_len):
                y_vals = [s[byte_idx] for s in share_data]
                
                
                secret_byte = ShamirSecretSharing._interpolate(x_vals, y_vals, 0)
                recovered.append(secret_byte)
            
            return bytes(recovered)
            
        except Exception as e:
            print(f"Shamir combine error: {e}")
            return None


# KATMAN 4: KRYPTOS ÇEKİRDEK (ŞİFRELEME MOTORU)


class KryptosCore:
    """Gelişmiş şifreleme motoru"""
    
    def __init__(self):
        self.backend = default_backend()
    
    def derive_key(self, password: str, salt: bytes, hwid: bytes, iterations: int = 1200000) -> bytes:
        """
        PBKDF2 ile anahtar türet (1.2M iterasyon)
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA512(),
            length=32,
            salt=salt,
            iterations=iterations,
            backend=self.backend
        )
        
        
        combined = password.encode() + hwid
        return base64.urlsafe_b64encode(kdf.derive(combined))
    
    def encrypt(self, data: bytes, key: bytes) -> bytes:
        """Fernet ile şifrele"""
        cipher = Fernet(key)
        return cipher.encrypt(data)
    
    def decrypt(self, data: bytes, key: bytes) -> bytes:
        """Fernet ile deşifre"""
        cipher = Fernet(key)
        return cipher.decrypt(data)
    
    def encrypt_aes(self, data: bytes, key: bytes) -> Tuple[bytes, bytes, bytes]:
        """AES-256-GCM ile şifrele (alternatif)"""
        iv = os.urandom(12)
        cipher = Cipher(
            algorithms.AES(key[:32]),
            modes.GCM(iv),
            backend=self.backend
        )
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(data) + encryptor.finalize()
        return ciphertext, iv, encryptor.tag


# KATMAN 5: OBSIDIAN BASTION (ANA SİSTEM)


class ObsidianBastion(GhostProtection):
    """Ana sistem çekirdeği"""
    
    def __init__(self, status_callback=None, progress_callback=None):
        super().__init__()
        
       
        self.kryptos = KryptosCore()
        self.shamir = ShamirSecretSharing
        
        self.vault_root = self._resolve_vault_path()
        self.offset_size = 512  
        self.shard_count = 100   
        self.shares_count = 5     
        self.threshold = 3        
        
        
        self.hwid = self._get_hardware_id()
        self.instance_id = hashlib.sha256(os.urandom(32)).hexdigest()[:16]
        
        
        self.failed_attempts = 0
        self.locked = False
        self.noise_stop = threading.Event()
        
        
        self.status_callback = status_callback
        self.progress_callback = progress_callback
        
       
        self._build_infrastructure()
        self._log_system_start()
    
    def _resolve_vault_path(self) -> str:
        """Platform bağımsız vault yolu"""
        folder = f".leviathan_{VERSION}"
        
        if self.os_name == "Windows":
            base = os.environ.get('LOCALAPPDATA', os.path.expanduser('~'))
            return os.path.join(base, folder)
        else:
            return os.path.expanduser(f"~/{folder}")
    
    def _build_infrastructure(self):
        """Klasör yapısını oluştur"""
        directories = [
            "shards",
            "shares",
            "logs",
            "temp",
            "backup",
            "manifests",
            "cache"
        ]
        
        for dir_name in directories:
            dir_path = os.path.join(self.vault_root, dir_name)
            if not os.path.exists(dir_path):
                if self.os_name != "Windows":
                    os.makedirs(dir_path, mode=0o700)
                else:
                    os.makedirs(dir_path)
        
        # (Windows)
        if self.os_name == "Windows":
            try:
                subprocess.call(["attrib", "+H", self.vault_root], 
                              shell=True, stderr=subprocess.DEVNULL)
            except:
                pass
    
    def _get_hardware_id(self) -> bytes:
        """Değişmez donanım kimliği oluştur"""
        components = []
        
        
        components.extend([
            platform.node(),
            platform.machine(),
            platform.system(),
            platform.processor()
        ])
        
       
        if self.os_name == "Linux":
            for path in ["/etc/machine-id", "/var/lib/dbus/machine-id"]:
                if os.path.exists(path):
                    try:
                        with open(path, 'r') as f:
                            components.append(f.read().strip())
                        break
                    except:
                        pass
        
       
        elif self.os_name == "Windows":
            try:
                # Volume serial
                result = subprocess.run(
                    ["cmd", "/c", "vol", "C:"],
                    capture_output=True,
                    text=True
                )
                components.append(result.stdout)
            except:
                pass
            
            try:
                
                import uuid
                mac = uuid.getnode()
                components.append(str(mac))
            except:
                pass
        
        
        raw = "|".join(components)
        return hashlib.sha3_512(raw.encode()).digest()
    
    def _log_system_start(self):
        """Sistem başlangıcını logla"""

        import datetime as dt

        log_entry = {
            
            "event": "SYSTEM_START",
            "version": VERSION,
            "instance": self.instance_id,
            "hwid": self.hwid.hex()[:16],
            "platform": self.os_name
        }
        self._log_event(log_entry)
    
    def _log_event(self, entry: dict):
        """Güvenli log kaydı"""
        try:
            log_path = os.path.join(self.vault_root, "logs", "bastion.log")
            with open(log_path, 'a') as f:
                f.write(json.dumps(entry) + '\n')
        except:
            pass
    
    def _update_status(self, message: str, color: str = "green"):
        """GUI status güncelleme"""
        if self.status_callback:
            self.status_callback(message, color)
    
    def _update_progress(self, value: int, maximum: int = 100):
        """GUI progress bar güncelleme"""
        if self.progress_callback:
            self.progress_callback(value, maximum)
    
    def process_shard(self, shard_id: int, data: bytes) -> Dict:
        """Tek bir shard'ı işle ve kaydet"""
        filename = f"shard_{shard_id:04d}.bin"
        filepath = os.path.join(self.vault_root, "shards", filename)
        
        
        noise = os.urandom(self.offset_size)
        final_data = noise + data
        
        
        with open(filepath, 'wb') as f:
            f.write(final_data)
        
        return {
            "id": shard_id,
            "file": filename,
            "hash": hashlib.sha3_256(final_data).hexdigest(),
            "size": len(final_data)
        }
    
    def seal(self, target_file: str, password: str) -> bool:
        """
        Dosyayı mühürle ve parçalara ayır
        """
        if not os.path.exists(target_file):
            self._update_status(f"Dosya bulunamadı: {target_file}", "red")
            return False
        
        self._update_status(f"🔒 Mühürleniyor: {os.path.basename(target_file)}", "blue")
        
        try:
            
            salt = os.urandom(32)
            
            
            master_key = self.kryptos.derive_key(password, salt, self.hwid)
            
            
            with open(target_file, 'rb') as f:
                file_data = f.read()
            
            
            metadata = {
                "filename": os.path.basename(target_file),
                "original_size": len(file_data),
                "timestamp": datetime.datetime.utcnow().isoformat(),
                "shard_count": self.shard_count,
                "shares_count": self.shares_count,
                "threshold": self.threshold,
                "hwid": self.hwid.hex(),
                "instance": self.instance_id,
                "version": VERSION
            }
            
            
            payload = {
                "metadata": metadata,
                "data": base64.b64encode(file_data).decode('ascii')
            }
            
            encrypted = self.kryptos.encrypt(
                json.dumps(payload).encode(),
                master_key
            )
            
            
            pad_length = (self.shard_count - (len(encrypted) % self.shard_count)) % self.shard_count
            encrypted += b'\x00' * pad_length
            

            shard_size = len(encrypted) // self.shard_count
            shards = [
                encrypted[i*shard_size:(i+1)*shard_size]
                for i in range(self.shard_count)
            ]
            
            
            manifest = {
                "salt": salt.hex(),
                "hwid": self.hwid.hex(),
                "pad": pad_length,
                "shards": []
            }
            
            self._update_status(f"📦 {self.shard_count} shard yazılıyor...", "blue")
            
            
            with ThreadPoolExecutor(max_workers=10) as executor:
                futures = []
                for i, shard in enumerate(shards):
                    future = executor.submit(self.process_shard, i, shard)
                    futures.append(future)
                    self._update_progress(i + 1, self.shard_count)
                
                for future in futures:
                    manifest["shards"].append(future.result())
            
            
            manifest_json = json.dumps(manifest).encode()
            shares = self.shamir.split(manifest_json, self.threshold, self.shares_count)
            
            if not shares:
                raise Exception("Shamir splitting failed")
            
            
            share_dir = os.path.join(self.vault_root, "shares")
            for share_id, share_data in shares:
                share_file = os.path.join(share_dir, f"share_{share_id:02d}.key")
                
                share_package = {
                    "id": share_id,
                    "data": base64.b64encode(share_data).decode('ascii'),
                    "threshold": self.threshold,
                    "total": self.shares_count,
                    "timestamp": datetime.datetime.utcnow().isoformat(),
                    "checksum": hashlib.sha256(share_data).hexdigest()[:16]
                }
                
                with open(share_file, 'w') as f:
                    json.dump(share_package, f, indent=2)
            
            
            self.secure_delete(target_file)
            
           
            self.secure_memory_wipe(master_key, encrypted, file_data, password)
            
            self._update_status(f"✅ BAŞARILI: {os.path.basename(target_file)} mühürlendi", "green")
            
           
            self._log_event({
                "timestamp": datetime.datetime.utcnow().isoformat(),
                "event": "SEAL_SUCCESS",
                "file": os.path.basename(target_file),
                "size": metadata["original_size"]
            })
            
            return True
            
        except Exception as e:
            self._update_status(f"❌ HATA: {str(e)}", "red")
            
            self._log_event({
                "timestamp": datetime.datetime.utcnow().isoformat(),
                "event": "SEAL_FAILED",
                "error": str(e)
            })
            
            return False
    
    def unseal(self, password: str) -> Optional[str]:
        """
        Mühürü aç ve dosyayı kurtar
        """
        if self.locked:
            self._update_status("🔒 Sistem kilitli!", "red")
            return None
        
        share_dir = os.path.join(self.vault_root, "shares")
        
        
        available_shares = []
        if os.path.exists(share_dir):
            for filename in os.listdir(share_dir):
                if filename.endswith(".key"):
                    try:
                        with open(os.path.join(share_dir, filename), 'r') as f:
                            share = json.load(f)
                            available_shares.append(share)
                    except:
                        continue
        
        if len(available_shares) < self.threshold:
            self._update_status(
                f"❌ Yeterli parça yok! ({len(available_shares)}/{self.threshold})",
                "red"
            )
            return None
        
        self._update_status(f"🔓 Kurtarma başlatılıyor...", "blue")
        
        try:
            
            shares_for_recovery = []
            for share in available_shares[:self.threshold]:
                share_data = base64.b64decode(share["data"])
                
                
                if hashlib.sha256(share_data).hexdigest()[:16] != share["checksum"]:
                    self._update_status(f"⚠ Parça {share['id']} bozulmuş!", "yellow")
                    continue
                
                shares_for_recovery.append((share["id"], share_data))
            
            if len(shares_for_recovery) < self.threshold:
                raise Exception(f"Yeterli sağlam parça yok: {len(shares_for_recovery)}")
            
            recovered_manifest = self.shamir.combine(shares_for_recovery)
            if not recovered_manifest:
                raise Exception("Manifest kurtarılamadı")
            
            manifest = json.loads(recovered_manifest)
            
            
            if manifest["hwid"] != self.hwid.hex():
                self.failed_attempts += 1
                self._update_status(f"❌ HWID uyuşmazlığı! ({self.failed_attempts}/3)", "red")
                
                if self.failed_attempts >= 3:
                    self.locked = True
                    self._update_status("🔒 SİSTEM KİLİTLENDİ!", "red")
                
                return None
            
            
            master_key = self.kryptos.derive_key(
                password,
                bytes.fromhex(manifest["salt"]),
                self.hwid
            )
            
            
            self._update_status("📦 Shard'lar toplanıyor...", "blue")
            shard_dir = os.path.join(self.vault_root, "shards")
            encrypted_parts = [None] * self.shard_count
            
            for idx, shard_info in enumerate(manifest["shards"]):
                shard_path = os.path.join(shard_dir, shard_info["file"])
                
                if not os.path.exists(shard_path):
                    raise Exception(f"Shard bulunamadı: {shard_info['file']}")
                
                with open(shard_path, 'rb') as f:
                    shard_data = f.read()
                
                
                current_hash = hashlib.sha3_256(shard_data).hexdigest()
                if current_hash != shard_info["hash"]:
                    raise Exception(f"Shard {shard_info['id']} bozulmuş!")
                
                
                encrypted_parts[shard_info["id"]] = shard_data[self.offset_size:]
                
                self._update_progress(idx + 1, self.shard_count)
            
            if None in encrypted_parts:
                raise Exception("Tüm shard'lar toplanamadı")
            
            
            encrypted_data = b"".join(encrypted_parts)
            
            
            if manifest["pad"] > 0:
                encrypted_data = encrypted_data[:-manifest["pad"]]
            
            
            decrypted = self.kryptos.decrypt(encrypted_data, master_key)
            payload = json.loads(decrypted.decode())
            
            
            output_file = payload["metadata"]["filename"]
            file_data = base64.b64decode(payload["data"])
            
            
            if os.path.exists(output_file):
                base, ext = os.path.splitext(output_file)
                counter = 1
                while os.path.exists(f"{base}_kurtarıldı{counter}{ext}"):
                    counter += 1
                output_file = f"{base}_kurtarıldı{counter}{ext}"
            
            with open(output_file, 'wb') as f:
                f.write(file_data)
            
            
            self.failed_attempts = 0
            self._update_status(f"✅ BAŞARILI: {os.path.basename(output_file)} kurtarıldı", "green")
            
           
            self._log_event({
                "timestamp": datetime.datetime.utcnow().isoformat(),
                "event": "UNSEAL_SUCCESS",
                "file": os.path.basename(output_file)
            })
            
            
            self.secure_memory_wipe(master_key, encrypted_data, file_data, password)
            
            return output_file
            
        except Exception as e:
            self.failed_attempts += 1
            self._update_status(f"❌ HATA: {str(e)} ({self.failed_attempts}/3)", "red")
            
            self._log_event({
                "timestamp": datetime.datetime.utcnow().isoformat(),
                "event": "UNSEAL_FAILED",
                "error": str(e)
            })
            
            if self.failed_attempts >= 3:
                self.locked = True
                self._update_status("🔒 SİSTEM KİLİTLENDİ!", "red")
            
            return None
    
    def get_status(self) -> Dict:
        """Sistem durumunu döndür"""
        status = {
            "version": VERSION,
            "platform": self.os_name,
            "hwid": self.hwid.hex()[:16],
            "instance": self.instance_id,
            "locked": self.locked,
            "failed_attempts": self.failed_attempts,
            "vault": self.vault_root,
            "protection": self.protection_active
        }
        
        
        shard_dir = os.path.join(self.vault_root, "shards")
        if os.path.exists(shard_dir):
            shards = [f for f in os.listdir(shard_dir) if f.startswith("shard_")]
            status["shards"] = len(shards)
        else:
            status["shards"] = 0
        
        
        share_dir = os.path.join(self.vault_root, "shares")
        if os.path.exists(share_dir):
            shares = [f for f in os.listdir(share_dir) if f.endswith(".key")]
            status["shares"] = len(shares)
        else:
            status["shares"] = 0
        
       
        if os.path.exists(self.vault_root):
            total = 0
            for root, dirs, files in os.walk(self.vault_root):
                total += sum(os.path.getsize(os.path.join(root, f)) for f in files)
            status["disk_usage"] = total
        
        return status
    
    def backup_shares(self, backup_dir: str) -> bool:
        """Shamir parçalarını yedekle"""
        share_dir = os.path.join(self.vault_root, "shares")
        
        if not os.path.exists(share_dir):
            self._update_status("❌ Yedeklenecek parça yok!", "red")
            return False
        
       
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_dir, f"leviathan_backup_{timestamp}")
        os.makedirs(backup_path, exist_ok=True)
        
        
        copied = 0
        for filename in os.listdir(share_dir):
            if filename.endswith(".key"):
                src = os.path.join(share_dir, filename)
                dst = os.path.join(backup_path, filename)
                shutil.copy2(src, dst)
                copied += 1
        
        self._update_status(f"✅ {copied} parça yedeklendi: {backup_path}", "green")
        
        self._log_event({
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "event": "BACKUP",
            "path": backup_path,
            "count": copied
        })
        
        return True
    
    def restore_shares(self, backup_dir: str) -> bool:
        """Shamir parçalarını geri yükle"""
        if not os.path.exists(backup_dir):
            self._update_status("❌ Yedek dizini bulunamadı!", "red")
            return False
        
        
        key_files = []
        for filename in os.listdir(backup_dir):
            if filename.endswith(".key"):
                key_files.append(filename)
        
        if not key_files:
            self._update_status("❌ Parça dosyası bulunamadı!", "red")
            return False
        
       
        share_dir = os.path.join(self.vault_root, "shares")
        if os.path.exists(share_dir):
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            old_backup = os.path.join(self.vault_root, "backup", f"old_shares_{timestamp}")
            os.makedirs(old_backup, exist_ok=True)
            
            for filename in os.listdir(share_dir):
                if filename.endswith(".key"):
                    src = os.path.join(share_dir, filename)
                    dst = os.path.join(old_backup, filename)
                    shutil.move(src, dst)
        
        # Yeni parçaları kopyala
        os.makedirs(share_dir, exist_ok=True)
        for filename in key_files:
            src = os.path.join(backup_dir, filename)
            dst = os.path.join(share_dir, filename)
            shutil.copy2(src, dst)
        
        self._update_status(f"✅ {len(key_files)} parça geri yüklendi", "green")
        
        self._log_event({
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "event": "RESTORE",
            "path": backup_dir,
            "count": len(key_files)
        })
        
        return True
    
    def self_destruct(self):
        """Kendini imha mekanizması"""
        self._update_status("💥 SELF-DESTRUCT ACTIVATED!", "red")
        
        try:
           
            shard_dir = os.path.join(self.vault_root, "shards")
            if os.path.exists(shard_dir):
                for filename in os.listdir(shard_dir):
                    filepath = os.path.join(shard_dir, filename)
                    self.secure_delete(filepath)
            
            
            share_dir = os.path.join(self.vault_root, "shares")
            if os.path.exists(share_dir):
                for filename in os.listdir(share_dir):
                    filepath = os.path.join(share_dir, filename)
                    self.secure_delete(filepath)
            
            
            log_dir = os.path.join(self.vault_root, "logs")
            if os.path.exists(log_dir):
                shutil.rmtree(log_dir)
            
            
            shutil.rmtree(self.vault_root, ignore_errors=True)
            
        except Exception as e:
            print(f"Self-destruct error: {e}")
        
        self._update_status("💥 SYSTEM PURGED", "red")


# KATMAN 6: GUI ARAYÜZÜ


class LeviathanGUI:
    """Grafiksel kullanıcı arayüzü"""
    
    def __init__(self, bastion: ObsidianBastion):
        self.bastion = bastion
        self.root = tk.Tk() 
        
        
        style = ttk.Style(self.root)
        style.theme_use('clam')
        style.configure(
            "green.Horizontal.TProgressbar",
            background=GUI_COLORS['success'],
            troughcolor='#333333',
            bordercolor=GUI_COLORS['success'],
            lightcolor=GUI_COLORS['success'],
            darkcolor=GUI_COLORS['success']
        )
        # -----------------------------------------------------------

        self.root.title(f"LEVIATHAN V{VERSION} - {CODENAME}")
        self.root.geometry("1000x750")
        self.root.configure(bg=GUI_COLORS['bg'])
        self.root.minsize(900, 650)
        
        
        self.password_var = tk.StringVar()
        self.confirm_var = tk.StringVar()
        self.selected_file = None
        self.operation_in_progress = False
        self.noise_stop = threading.Event()
        self.jammer_thread = None
        self.last_dir = None
        
        
        self._setup_fonts()
        self._setup_ui()
        self._setup_hotkeys()
        self._start_jammer()

        
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)


        self.root.bind("<Escape>", self.panic_kill_switch)

        self.root.bind_all("<Control-Shift-V>", self._check_developer_auth)

        try:
            
            self.root.iconbitmap("main.ico")
        except Exception as e:
            
            print(f"[*] İkon yüklenemedi (Dosya bulunamadı mı?): {e}")


       
        self.root.after(500, self.show_startup_intel)


    def panic_kill_switch(self, event=None):
        """
        [ EMERGENCY PROTOCOL: SIGTERM ]
        ESC tuşu tetiklendiğinde tüm işlemleri durdurur ve iz bırakmadan kapanır.
        """
        try:
            
            self.update_log("!!! KILL-SWITCH TETIKLENDI !!!", "error")
            self.update_log("Bellek imha ediliyor...", "warning")
            
           
            import gc
            import os
            
            
            gc.collect() 
            
            
            self.root.configure(bg="#ff0000")
            self.root.update()
            
           
            self.root.destroy()
            
            
            os._exit(0)
            
        except Exception:
            
            import os
            os._exit(1)


    def run(self):
        self.root.mainloop()

    def _setup_fonts(self):
        """Fontları ayarla"""
        self.fonts = {
            'title': Font(family="Consolas", size=18, weight="bold"),
            'heading': Font(family="Consolas", size=12, weight="bold"),
            'normal': Font(family="Consolas", size=10),
            'small': Font(family="Consolas", size=8),
            'mono': Font(family="Courier", size=10)
        }
    
    def _setup_hotkeys(self):
        """Klavye kısayolları"""
        self.root.bind('<Control-o>', lambda e: self.select_file())
        self.root.bind('<Control-s>', lambda e: self.seal_file())
        self.root.bind('<Control-u>', lambda e: self.unseal_file())
        self.root.bind('<Control-q>', lambda e: self._on_closing())
        self.root.bind('<F1>', lambda e: self.show_help())
    
    def _start_jammer(self):
        """Neural jammer'ı başlat"""
        self.noise_stop.clear()
        self.jammer_thread = threading.Thread(
            target=self.bastion.neural_jammer,
            args=(self.noise_stop,),
            daemon=True
        )
        self.jammer_thread.start()
    
    def show_startup_intel(self):
        """Uygulama açılışında otomatik gösterilen, 5 saniye kilitli bilgi penceresi"""
        startup_win = tk.Toplevel(self.root)
        startup_win.title("LEVIATHAN - INITIALIZATION BRIEFING")
        startup_win.geometry("550x620")
        startup_win.configure(bg=GUI_COLORS['bg'])
        startup_win.resizable(False, False)
        
        
        startup_win.grab_set() 

        header = tk.Label(startup_win, text="[ CLASSIFIED SYSTEM BRIEFING ]", 
                         bg=GUI_COLORS['bg'], fg=GUI_COLORS['success'], 
                         font=("Consolas", 14, "bold"), pady=20)
        header.pack()

        intel_text = """
> DURUM: SISTEM AKTIF
> SURUM: V1.0 (SINGULARITY)
> GUVENLIK SEVIYESI: MAXIMUM

[ KULLANIM TALIMATLARI ]
1. DOSYA SECIMI: Muhurlemek istediginiz veriyi belirleyin.
2. ANAHTAR OLUSTURMA: En az 12 haneli, karmasik bir sifre girin.
3. MUHURLEME: Islem basladiginda veriniz 100 parcaya bolunur.
4. IMHA: Orijinal dosya sistemden kalici olarak silinir.

[ KRITIK UYARI ]
Sifrenizi kaybetmeniz durumunda veri kurtarma imkansizdir. 
Leviathan'ın arka kapısı (backdoor) yoktur.

NOT:Sistem Üst Düzey Güvenlik Sistemleri sebeplerinden dolayı ağır çalışabilir.
(Lütfen Sabırlı Olun)

        """

        text_area = tk.Text(startup_win, bg="#0a0a0a", fg=GUI_COLORS['fg'], 
                           font=("Consolas", 10), wrap=tk.WORD, padx=15, pady=15, 
                           borderwidth=1, relief=tk.SOLID)
        text_area.insert(tk.END, intel_text)
        text_area.config(state=tk.DISABLED)
        text_area.pack(padx=20, fill=tk.BOTH, expand=True)

        self.accept_btn = tk.Button(startup_win, text="[ BEKLEYİN (5) ]", 
                                   command=startup_win.destroy,
                                   state=tk.DISABLED, # Kilitli başla
                                   bg=GUI_COLORS['bg'], fg="gray", 
                                   font=("Consolas", 10, "bold"), 
                                   activebackground=GUI_COLORS['success'],
                                   relief=tk.GROOVE, borderwidth=2)
        self.accept_btn.pack(pady=20)

        def count_down(remaining):
            if remaining > 0:
                self.accept_btn.config(text=f"[ BEKLEYİN ({remaining}) ]")
                startup_win.after(1000, lambda: count_down(remaining - 1))
            else:
                self.accept_btn.config(state=tk.NORMAL, text="[ PROTOKOLLERI KABUL ET ]", 
                                       fg=GUI_COLORS['success'], cursor="hand2")
        
        
        count_down(5)



    def _stop_jammer(self):
        """Jammer'ı durdur"""
        self.noise_stop.set()
    
    def _setup_ui(self):
        """Ana arayüzü kur"""
        main_container = tk.Frame(self.root, bg=GUI_COLORS['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self._setup_header(main_container)
        
        content_frame = tk.Frame(main_container, bg=GUI_COLORS['bg'])
        content_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        left_panel = tk.Frame(content_frame, bg=GUI_COLORS['panel'], width=350)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10))
        left_panel.pack_propagate(False)
        
        right_panel = tk.Frame(content_frame, bg=GUI_COLORS['panel'])
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self._setup_file_selection(left_panel)
        self._setup_password_input(left_panel)
        self._setup_operations(left_panel)
        self._setup_system_info(left_panel)
        self._setup_log_area(right_panel)
        
        self._setup_status_bar(main_container)

        self.watermark = tk.Label(
            self.root, 
            text="ORIGINAL EDITION BY THEVAL3X",
            bg=GUI_COLORS['bg'],
            fg="#d11414",
            font=("Consolas", 8, "italic")
        )
        self.watermark.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)
        
        tiktok_frame = tk.Frame(
            self.root,
            bg='#ff0050',  
            bd=1,
            relief=tk.RAISED
        )
        tiktok_frame.place(relx=0.0, rely=0.0, anchor="nw", x=8, y=8)
        
        self.tiktok_btn = tk.Button(
            tiktok_frame,
            text="🎵 TikTok'ta Takip Et",
            command=self.open_tiktok,
            bg='#000000',
            fg='#ff0050',
            font=("Consolas", 8, "bold"),
            relief=tk.FLAT,
            cursor='hand2',
            padx=8,
            pady=4,
            activebackground='#ff0050',
            activeforeground='white'
        )
        self.tiktok_btn.pack()
        
        def on_tiktok_enter(e):
            self.tiktok_btn.config(bg='#ff0050', fg='white')
            tiktok_frame.config(bg='white')
        
        def on_tiktok_leave(e):
            self.tiktok_btn.config(bg='#000000', fg='#ff0050')
            tiktok_frame.config(bg='#ff0050')
        
        self.tiktok_btn.bind("<Enter>", on_tiktok_enter)
        self.tiktok_btn.bind("<Leave>", on_tiktok_leave)
        tiktok_frame.bind("<Enter>", on_tiktok_enter)
        tiktok_frame.bind("<Leave>", on_tiktok_leave)
        
        self.watermark.lift()
        tiktok_frame.lift()


    def open_tiktok(self):
        """TikTok hesabını tarayıcıda aç"""
        tiktok_username = "valexinmade0q"  
        tiktok_url = f"https://www.tiktok.com/@{tiktok_username}"
        
        try:
            if platform.system() == "Windows":
                os.startfile(tiktok_url)
            elif platform.system() == "Linux":
                subprocess.Popen(["xdg-open", tiktok_url])
            elif platform.system() == "Darwin":  # macOS
                subprocess.Popen(["open", tiktok_url])
            
            self.update_status(f"🎵 @{tiktok_username} açılıyor...", "blue")
            self.log(f"TikTok hesabı açıldı: @{tiktok_username}", "info")
            
        except Exception as e:
            self.update_status(f"❌ TikTok açılamadı", "red")
            self.log(f"TikTok hatası: {str(e)}", "error")


    

    


        
    
    def _setup_header(self, parent):
        """Başlık alanı"""
        header = tk.Frame(parent, bg=GUI_COLORS['panel'], height=120)
        header.pack(fill=tk.X, pady=(0, 10))
        header.pack_propagate(False)
        
        # ASCII Banner
        banner = """███████╗██╗     ███████╗██╗   ██╗██╗ █████╗ ████████╗██╗  ██╗ █████╗ ███╗   ██╗
██╔════╝██║     ██╔════╝██║   ██║██║██╔══██╗╚══██╔══╝██║  ██║██╔══██╗████╗  ██║
█████╗  ██║     █████╗  ██║   ██║██║███████║   ██║   ███████║███████║██╔██╗ ██║
██╔══╝  ██║     ██╔══╝  ╚██╗ ██╔╝██║██╔══██║   ██║   ██╔══██║██╔══██║██║╚██╗██║
███████╗███████╗███████╗ ╚████╔╝ ██║██║  ██║   ██║   ██║  ██║██║  ██║██║ ╚████║
╚══════╝╚══════╝╚══════╝  ╚═══╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝"""
        
        banner_label = tk.Label(
            header,
            text=banner,
            font=self.fonts['small'],
            fg=GUI_COLORS['fg'],
            bg=GUI_COLORS['panel'],
            justify=tk.LEFT
        )
        banner_label.pack(pady=5)
        
        info_frame = tk.Frame(header, bg=GUI_COLORS['panel'])
        info_frame.pack()
        
        version_text = f"V{VERSION} | SHAMIR: {self.bastion.threshold}/{self.bastion.shares_count} | SHARDS: {self.bastion.shard_count} | HWID: {self.bastion.hwid.hex()[:16]}..."
        
        tk.Label(
            info_frame,
            text=version_text,
            font=self.fonts['small'],
            fg=GUI_COLORS['accent'],
            bg=GUI_COLORS['panel']
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Label(
            info_frame,
            text="🔒 KERNEL SHIELD ACTIVE",
            font=self.fonts['small'],
            fg=GUI_COLORS['success'],
            bg=GUI_COLORS['panel']
        ).pack(side=tk.LEFT, padx=5)

        

    def _setup_file_selection(self, parent):
        """Dosya seçim alanı"""
        frame = tk.LabelFrame(
            parent,
            text="📁 DOSYA SEÇİMİ",
            bg=GUI_COLORS['panel'],
            fg=GUI_COLORS['fg'],
            font=self.fonts['heading']
        )
        frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.file_label = tk.Label(
            frame,
            text="Henüz dosya seçilmedi",
            bg=GUI_COLORS['panel'],
            fg='#666666',
            font=self.fonts['normal'],
            wraplength=300
        )
        self.file_label.pack(pady=5)
        
        btn_frame = tk.Frame(frame, bg=GUI_COLORS['panel'])
        btn_frame.pack(pady=5)
        
        select_btn = tk.Button(
            btn_frame,
            text="📂 DOSYA SEÇ",
            command=self.select_file,
            bg='#333333',
            fg=GUI_COLORS['fg'],
            font=self.fonts['normal'],
            relief=tk.FLAT,
            cursor='hand2',
            width=15
        )
        select_btn.pack(side=tk.LEFT, padx=2)
        
        clear_btn = tk.Button(
            btn_frame,
            text="🗑 TEMİZLE",
            command=self.clear_file,
            bg='#333333',
            fg=GUI_COLORS['fg'],
            font=self.fonts['normal'],
            relief=tk.FLAT,
            cursor='hand2',
            width=10
        )
        clear_btn.pack(side=tk.LEFT, padx=2)
    
    def _setup_password_input(self, parent):
        """Şifre giriş alanı"""
        frame = tk.LabelFrame(
            parent,
            text="🔐 ŞİFRE GİRİŞİ",
            bg=GUI_COLORS['panel'],
            fg=GUI_COLORS['fg'],
            font=self.fonts['heading']
        )
        frame.pack(fill=tk.X, padx=10, pady=5)
        
        pw_frame = tk.Frame(frame, bg=GUI_COLORS['panel'])
        pw_frame.pack(fill=tk.X, padx=5, pady=2)
        
        tk.Label(
            pw_frame,
            text="Şifre:",
            bg=GUI_COLORS['panel'],
            fg=GUI_COLORS['text'],
            font=self.fonts['normal'],
            width=10,
            anchor=tk.W
        ).pack(side=tk.LEFT)
        
        self.password_entry = tk.Entry(
            pw_frame,
            textvariable=self.password_var,
            show="●",
            bg='#333333',
            fg=GUI_COLORS['fg'],
            font=self.fonts['normal'],
            insertbackground=GUI_COLORS['fg'],
            width=25
        )
        self.password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        confirm_frame = tk.Frame(frame, bg=GUI_COLORS['panel'])
        confirm_frame.pack(fill=tk.X, padx=5, pady=2)
        
        tk.Label(
            confirm_frame,
            text="Tekrar:",
            bg=GUI_COLORS['panel'],
            fg=GUI_COLORS['text'],
            font=self.fonts['normal'],
            width=10,
            anchor=tk.W
        ).pack(side=tk.LEFT)
        
        self.confirm_entry = tk.Entry(
            confirm_frame,
            textvariable=self.confirm_var,
            show="●",
            bg='#333333',
            fg=GUI_COLORS['fg'],
            font=self.fonts['normal'],
            insertbackground=GUI_COLORS['fg'],
            width=25
        )
        self.confirm_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    def _setup_operations(self, parent):
        """Operasyon butonları + Tema seçici"""
        frame = tk.LabelFrame(
            parent,
            text="⚡ OPERASYONLAR",
            bg=GUI_COLORS['panel'],
            fg=GUI_COLORS['fg'],
            font=self.fonts['heading']
        )
        frame.pack(fill=tk.X, padx=10, pady=5)
        
        btn_frame = tk.Frame(frame, bg=GUI_COLORS['panel'])
        btn_frame.pack(pady=10)
        
        self.seal_btn = tk.Button(
            btn_frame,
            text="🔒 MÜHÜRLE (SEAL)",
            command=self.seal_file,
            bg='#004400',
            fg='white',
            font=self.fonts['normal'],
            relief=tk.FLAT,
            cursor='hand2',
            width=20,
            height=2
        )
        self.seal_btn.pack(pady=2)
        
        self.unseal_btn = tk.Button(
            btn_frame,
            text="🔓 KURTAR (UNSEAL)",
            command=self.unseal_file,
            bg='#004466',
            fg='white',
            font=self.fonts['normal'],
            relief=tk.FLAT,
            cursor='hand2',
            width=20,
            height=2
        )
        self.unseal_btn.pack(pady=2)
        
        sec_frame = tk.Frame(frame, bg=GUI_COLORS['panel'])
        sec_frame.pack(pady=5)
        
        backup_btn = tk.Button(
            sec_frame,
            text="💾 YEDEKLE",
            command=self.backup_shares,
            bg='#333333',
            fg=GUI_COLORS['fg'],
            font=self.fonts['small'],
            relief=tk.FLAT,
            cursor='hand2',
            width=10
        )
        backup_btn.pack(side=tk.LEFT, padx=2)
        
        restore_btn = tk.Button(
            sec_frame,
            text="🔄 GERİ YÜKLE",
            command=self.restore_shares,
            bg='#333333',
            fg=GUI_COLORS['fg'],
            font=self.fonts['small'],
            relief=tk.FLAT,
            cursor='hand2',
            width=10
        )
        restore_btn.pack(side=tk.LEFT, padx=2)
        
        theme_frame = tk.LabelFrame(
            frame,
            text="🎨 TEMA SEÇİN",
            bg=GUI_COLORS['panel'],
            fg=GUI_COLORS['fg'],
            font=self.fonts['small']
        )
        theme_frame.pack(fill=tk.X, padx=5, pady=5)
        
        theme_buttons_frame = tk.Frame(theme_frame, bg=GUI_COLORS['panel'])
        theme_buttons_frame.pack(pady=5)
        
        self.dark_btn = tk.Button(
            theme_buttons_frame,
            text="🌑 KARANLIK",
            command=lambda: self.change_theme('karanlık'),
            bg=THEMES['karanlık']['panel'],
            fg=THEMES['karanlık']['fg'],
            font=self.fonts['small'],
            relief=tk.FLAT,
            cursor='hand2',
            width=10
        )
        self.dark_btn.grid(row=0, column=0, padx=2, pady=2)
        
        self.light_btn = tk.Button(
            theme_buttons_frame,
            text="☀️ AYDINLIK",
            command=lambda: self.change_theme('aydınlık'),
            bg=THEMES['aydınlık']['panel'],
            fg=THEMES['aydınlık']['text'],
            font=self.fonts['small'],
            relief=tk.FLAT,
            cursor='hand2',
            width=10
        )
        self.light_btn.grid(row=0, column=1, padx=2, pady=2)
        
        self.matrix_btn = tk.Button(
            theme_buttons_frame,
            text="💚 MATRİX",
            command=lambda: self.change_theme('matrix'),
            bg=THEMES['matrix']['button'],
            fg=THEMES['matrix']['fg'],
            font=self.fonts['small'],
            relief=tk.FLAT,
            cursor='hand2',
            width=10
        )
        self.matrix_btn.grid(row=1, column=0, padx=2, pady=2)
        
        self.hacker_btn = tk.Button(
            theme_buttons_frame,
            text="🔥 HACKER",
            command=lambda: self.change_theme('hacker'),
            bg=THEMES['hacker']['button'],
            fg=THEMES['hacker']['fg'],
            font=self.fonts['small'],
            relief=tk.FLAT,
            cursor='hand2',
            width=10
        )
        self.hacker_btn.grid(row=1, column=1, padx=2, pady=2)
        
        for btn in [self.dark_btn, self.light_btn, self.matrix_btn, self.hacker_btn]:
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg='#666666', fg='white'))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=b['bg'], fg=b['fg']))
        
        self.theme_indicator = tk.Label(
            theme_frame,
            text=f"✓ Aktif: {THEMES[CURRENT_THEME]['name']}",
            bg=GUI_COLORS['panel'],
            fg=GUI_COLORS['success'],
            font=self.fonts['small']
        )
        self.theme_indicator.pack(pady=2)
        
        danger_frame = tk.Frame(frame, bg=GUI_COLORS['panel'])
        danger_frame.pack(pady=5)
        
        status_btn = tk.Button(
            danger_frame,
            text="📊 DURUM",
            command=self.show_status,
            bg='#333333',
            fg=GUI_COLORS['fg'],
            font=self.fonts['small'],
            relief=tk.FLAT,
            cursor='hand2',
            width=10
        )
        status_btn.pack(side=tk.LEFT, padx=2)
        
        self.destruct_btn = tk.Button(
            danger_frame,
            text="💥 İMHA",
            command=self.self_destruct,
            bg='#440000',
            fg='white',
            font=self.fonts['small'],
            relief=tk.FLAT,
            cursor='hand2',
            width=10
        )
        self.destruct_btn.pack(side=tk.LEFT, padx=2)
        
        status_btn.bind("<Enter>", lambda e: status_btn.config(bg='#555555'))
        status_btn.bind("<Leave>", lambda e: status_btn.config(bg='#333333'))
        self.destruct_btn.bind("<Enter>", lambda e: self.destruct_btn.config(bg='#660000'))
        self.destruct_btn.bind("<Leave>", lambda e: self.destruct_btn.config(bg='#440000'))
    
    def _setup_system_info(self, parent):
        """Sistem bilgileri"""
        frame = tk.LabelFrame(
            parent,
            text="ℹ SİSTEM BİLGİSİ",
            bg=GUI_COLORS['panel'],
            fg=GUI_COLORS['fg'],
            font=self.fonts['heading']
        )
        frame.pack(fill=tk.X, padx=10, pady=5)
        
        info_text = f"""
Platform:    {self.bastion.os_name}
Koruma:      {'✅ AKTİF' if self.bastion.protection_active else '❌ PASİF'}
Vault:       {self.bastion.vault_root}
Shards:      {self.bastion.shard_count}
Shares:      {self.bastion.shares_count} (Eşik: {self.bastion.threshold})
        """
        
        tk.Label(
            frame,
            text=info_text,
            bg=GUI_COLORS['panel'],
            fg=GUI_COLORS['text'],
            font=self.fonts['small'],
            justify=tk.LEFT
        ).pack(padx=5, pady=5, anchor=tk.W)
    
    def _setup_log_area(self, parent):
        """Log alanı - ASCII Banner ve Dinamik Log Akışı"""
        frame = tk.LabelFrame(
            parent,
            text="📋 OPERASYON LOGU",
            bg=GUI_COLORS['panel'],
            fg=GUI_COLORS['fg'],
            font=self.fonts['heading']
        )
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        banner_text = """
    __    _______    _________  ______  __  ___
   / /   / ____/ |  / /  _/   |/_  __/ / / / /
  / /   / __/  | | / // // /| | / /   / / / / 
 / /___/ /___  | |/ // // ___ |/ /   / /_/ /  
/_____/_____/  |___/___/_/  |_/_/    \\____/   
[ SYSTEM STATUS: OPERATIONAL ] [ VERSION: 1.0 ]
    "Kırılması İmkansıza Yakın Güvenlik!"
        """
        self.banner_label = tk.Label(
            frame,
            text=banner_text,
            bg=GUI_COLORS['panel'],
            fg=GUI_COLORS['success'], 
            font=("Consolas", 7, "bold"),
            justify=tk.LEFT,
            pady=5
        )
        self.banner_label.pack(fill=tk.X)

        separator = tk.Frame(frame, height=1, bg="#333333")
        separator.pack(fill=tk.X, padx=5, pady=2)

        self.log_text = scrolledtext.ScrolledText(
            frame,
            bg=GUI_COLORS['dark'],
            fg=GUI_COLORS['fg'],
            font=self.fonts['mono'],
            state=tk.DISABLED,
            wrap=tk.WORD,
            height=15
            insertbackground=GUI_COLORS['fg'],
            borderwidth=0,
            highlightthickness=0
        )
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.log_text.tag_config("timestamp", foreground="#666666")
        self.log_text.tag_config("success", foreground="#00ff00")
        self.log_text.tag_config("error", foreground="#ff0000")
        self.log_text.tag_config("warning", foreground="#ffaa00")
        self.log_text.tag_config("info", foreground="#00aaff")
        
        btn_frame = tk.Frame(frame, bg=GUI_COLORS['panel'])
        btn_frame.pack(fill=tk.X, padx=5, pady=5)
        
        btn_style = {
            "bg": "#1a1a1a",
            "fg": GUI_COLORS['fg'],
            "font": self.fonts['small'],
            "relief": tk.FLAT,
            "cursor": "hand2",
            "activebackground": GUI_COLORS['success'],
            "activeforeground": "black"
        }

        clear_log_btn = tk.Button(
            btn_frame,
            text="🧹 LOG TEMİZLE",
            command=self.clear_log,
            **btn_style
        )
        clear_log_btn.pack(side=tk.LEFT, padx=2)
        
        save_log_btn = tk.Button(
            btn_frame,
            text="💾 LOG KAYDET",
            command=self.save_log,
            **btn_style
        )
        save_log_btn.pack(side=tk.LEFT, padx=2)

        clear_log_btn.bind("<Enter>", lambda e: clear_log_btn.config(bg="#333333"))
        clear_log_btn.bind("<Leave>", lambda e: clear_log_btn.config(bg="#1a1a1a"))
        save_log_btn.bind("<Enter>", lambda e: save_log_btn.config(bg="#333333"))
        save_log_btn.bind("<Leave>", lambda e: save_log_btn.config(bg="#1a1a1a"))
    
    def _setup_status_bar(self, parent):
        """Durum çubuğu"""
        status_bar = tk.Frame(parent, bg=GUI_COLORS['panel'], height=30)
        status_bar.pack(fill=tk.X, pady=(5, 0))
        status_bar.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_bar,
            text="✅ SİSTEM HAZIR",
            bg=GUI_COLORS['panel'],
            fg=GUI_COLORS['success'],
            font=self.fonts['normal']
        )
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        right_frame = tk.Frame(status_bar, bg=GUI_COLORS['panel'])
        right_frame.pack(side=tk.RIGHT, padx=10)
        
        self.progress = ttk.Progressbar(
            right_frame,
            mode='determinate',
            length=150,
            style='green.Horizontal.TProgressbar'
        )
        self.progress.pack(side=tk.LEFT, padx=5)
        
        self.progress_label = tk.Label(
            right_frame,
            text="0%",
            bg=GUI_COLORS['panel'],
            fg=GUI_COLORS['fg'],
            font=self.fonts['small']
        )
        self.progress_label.pack(side=tk.LEFT)
    
    
    def log(self, message: str, tag: str = "info"):
        """Log mesajı ekle (Kilit Yönetimi ve Datetime Hatası Giderilmiş Versiyon)"""
        import datetime as dt_module # Çakışmaları önlemek için lokal import
        
        try:
            
            now = dt_module.datetime.now()
            timestamp = now.strftime("%H:%M:%S")
            
            print(f"[{timestamp}] [{tag.upper()}] {message}")

            if hasattr(self, 'log_text'):
                self.log_text.config(state='normal') # Yazma kilidini aç
                self.log_text.insert(tk.END, f"[{timestamp}] ", "timestamp")
                self.log_text.insert(tk.END, f"{message}\n", tag)
                self.log_text.config(state='disabled') # Kilidi geri tak (Salt okunur yap)
                self.log_text.see(tk.END) # En alta kaydır
                
        except Exception as e:
            print(f"!!! LOG SİSTEMİ HATASI: {e}")
        
    
    def update_status(self, message: str, color: str = "green"):
        """Status güncelle"""
        color_map = {
            "green": GUI_COLORS['success'],
            "red": GUI_COLORS['error'],
            "blue": GUI_COLORS['accent'],
            "yellow": GUI_COLORS['warning']
        }
        
        self.status_label.config(text=message, fg=color_map.get(color, GUI_COLORS['fg']))
        
        tag_map = {
            "green": "success",
            "red": "error",
            "blue": "info",
            "yellow": "warning"
        }
        
        self.log(message, tag_map.get(color, "info"))
    
    def update_progress(self, value: int, maximum: int = 100):
        """Progress bar güncelle"""
        self.progress['maximum'] = maximum
        self.progress['value'] = value
        percent = int((value / maximum) * 100) if maximum > 0 else 0
        self.progress_label.config(text=f"{percent}%")
        self.root.update()
    
    def select_file(self):
        """Dosya seç - Tüm dosya türleri destekli"""
        
        if hasattr(self, 'last_dir') and self.last_dir:
            initial_dir = self.last_dir
        else:
            initial_dir = os.path.expanduser("~")
            if platform.system() == "Windows":
                docs = os.path.join(initial_dir, "Documents")
                if os.path.exists(docs):
                    initial_dir = docs
        
        filename = filedialog.askopenfilename(
            title="Dosya Seç - Leviathan",
            initialdir=initial_dir,
            filetypes=[
                ("Tüm dosyalar", "*.*"),
                ("--------------------------------", "*"),
                ("📷 RESİMLER", "*.jpg *.jpeg *.png *.gif *.bmp *.ico *.svg *.webp *.tiff"),
                ("🎵 SES DOSYALARI", "*.mp3 *.wav *.flac *.aac *.ogg *.wma *.m4a"),
                ("🎬 VİDEOLAR", "*.mp4 *.avi *.mkv *.mov *.wmv *.flv *.webm *.m4v"),
                ("📄 BELGELER", "*.pdf *.doc *.docx *.txt *.rtf *.odt *.xls *.xlsx *.ppt *.pptx"),
                ("🗜️ ARŞİVLER", "*.zip *.rar *.7z *.tar *.gz *.bz2 *.xz"),
                ("💻 PROGRAMLAR", "*.exe *.msi *.deb *.rpm *.app *.dmg"),
                ("🌐 WEB DOSYALARI", "*.html *.htm *.css *.js *.php *.asp"),
                ("📚 KİTAPLAR", "*.epub *.mobi *.azw *.cbr *.cbz"),
                ("🎨 GRAFİK TASARIM", "*.psd *.ai *.cdr *.xd *.fig *.sketch"),
                ("📊 VERİTABANI", "*.sql *.db *.sqlite *.mdb *.accdb"),
                ("⚙️ SİSTEM DOSYALARI", "*.dll *.so *.dylib *.sys *.ini *.cfg"),
                ("📜 KOD DOSYALARI", "*.py *.java *.c *.cpp *.h *.cs *.php *.rb *.go *.rs"),
                ("📝 METİN DOSYALARI", "*.txt *.log *.md *.rst *.tex"),
                ("📈 VERİ DOSYALARI", "*.csv *.json *.xml *.yaml *.yml"),
            ]
        )
        
        if filename:
            self.selected_file = os.path.normpath(filename)
            self.last_dir = os.path.dirname(filename)
            
            self.file_label.config(
                text=os.path.basename(self.selected_file),
                fg=GUI_COLORS['fg']
            )
            
            ext = os.path.splitext(filename)[1].lower()
            emoji = "📄"  
            if ext in ['.jpg','.jpeg','.png','.gif']:
                emoji = "📷"
            elif ext in ['.mp3','.wav']:
                emoji = "🎵"
            elif ext in ['.mp4','.avi']:
                emoji = "🎬"
            elif ext in ['.pdf']:
                emoji = "📕"
            elif ext in ['.zip','.rar']:
                emoji = "🗜️"
            elif ext in ['.exe']:
                emoji = "⚙️"
            elif ext in ['.py']:
                emoji = "🐍"
            
            self.update_status(f"{emoji} Dosya seçildi: {os.path.basename(self.selected_file)}", "green")
    
    def clear_file(self):
        """Dosya seçimini temizle"""
        self.selected_file = None
        self.file_label.config(text="Henüz dosya seçilmedi", fg='#666666')
        self.update_status("🧹 Dosya seçimi temizlendi", "blue")
    
    def clear_log(self):
        """Log ekranını temizle"""
        self.log_text.delete(1.0, tk.END)
        self.update_status("🧹 Log temizlendi", "blue")
    
    def save_log(self):
        """Log'u dosyaya kaydet"""
        filename = filedialog.asksaveasfilename(
            title="Log Kaydet",
            defaultextension=".log",
            filetypes=[("Log files", "*.log"), ("Text files", "*.txt"), ("Tüm dosyalar", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w') as f:
                    f.write(self.log_text.get(1.0, tk.END))
                self.update_status(f"✅ Log kaydedildi: {filename}", "green")
            except Exception as e:
                self.update_status(f"❌ Log kaydedilemedi: {e}", "red")
    
    def show_help(self):
        """Yardım penceresi"""
        help_text = f"""
LEVIATHAN V{VERSION} - {CODENAME}

KLAVYE KISAYOLLARI:
------------------
Ctrl+O : Dosya seç
Ctrl+S : Mühürle (SEAL)
Ctrl+U : Kurtar (UNSEAL)
Ctrl+Q : Çıkış
F1     : Bu yardım penceresi

GÜVENLİK ÖZELLİKLERİ:
--------------------
🔒 Kernel seviyesi koruma (Linux/Windows)
🔒 1.2M iterasyon PBKDF2 anahtar türetme
🔒 HWID tabanlı yetkilendirme
🔒 Shamir Secret Sharing (3/5 eşik)
🔒 100 parçaya bölme + gürültü
🔒 Anti-forensic bellek temizliği
🔒 Neural Jammer (keylogger koruması)
🔒 3 başarısız denemede self-destruct

KULLANIM:
--------
1. Bir dosya seçin
2. Güçlü bir şifre girin
3. "MÜHÜRLE" ile dosyayı şifreleyin
4. "KURTAR" ile geri getirin

VAULT KONUMU: {self.bastion.vault_root}
        """
        
        help_win = tk.Toplevel(self.root)
        help_win.title("LEVIATHAN - YARDIM")
        help_win.geometry("600x500")
        help_win.configure(bg=GUI_COLORS['bg'])
        
        text_area = scrolledtext.ScrolledText(
            help_win,
            bg=GUI_COLORS['dark'],
            fg=GUI_COLORS['fg'],
            font=self.fonts['mono'],
            wrap=tk.WORD
        )
        text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        text_area.insert(1.0, help_text)
        text_area.config(state=tk.DISABLED)
    
    def show_status(self):
        """Sistem durumu penceresi"""
        status = self.bastion.get_status()
        
        status_text = f"""
LEVIATHAN V{VERSION} - SİSTEM DURUMU
{'='*50}

GENEL BİLGİLER:
--------------
Platform:    {status['platform']}
HWID:        {status['hwid']}
Instance:    {status['instance']}
Kilitli:     {'EVET' if status['locked'] else 'HAYIR'}
Koruma:      {'AKTİF' if status['protection'] else 'PASİF'}
Başarısız:   {status['failed_attempts']}/3

VAULT BİLGİLERİ:
---------------
Konum:       {status['vault']}
Shards:      {status.get('shards', 0)}/{self.bastion.shard_count}
Shares:      {status.get('shares', 0)}/{self.bastion.shares_count}
Disk:        {status.get('disk_usage', 0):,} bytes

ZAMAN BİLGİSİ:
-------------
Şu an:       {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        status_win = tk.Toplevel(self.root)
        status_win.title("SİSTEM DURUMU")
        status_win.geometry("600x500")
        status_win.configure(bg=GUI_COLORS['bg'])
        
        text_area = scrolledtext.ScrolledText(
            status_win,
            bg=GUI_COLORS['dark'],
            fg=GUI_COLORS['fg'],
            font=self.fonts['mono'],
            wrap=tk.WORD
        )
        text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        text_area.insert(1.0, status_text)
        text_area.config(state=tk.DISABLED)
    
    def seal_file(self):
        """Mühürleme işlemi"""
        if self.operation_in_progress:
            self.update_status("⚠ İşlem zaten devam ediyor!", "yellow")
            return
        
        if not self.selected_file:
            self.update_status("❌ Lütfen bir dosya seçin!", "red")
            messagebox.showwarning("Uyarı", "Lütfen bir dosya seçin!")
            return
        
        password = self.password_entry.get() 
        confirm = self.confirm_entry.get()
        
        if len(password) < 6:
            self.update_status("❌ Şifre en az 6 karakter olmalı!", "red")
            messagebox.showwarning("Uyarı", "Şifre en az 6 karakter olmalı!\nDaha güvenli için 12+ karakter önerilir.")
            return


        if not password:
            self.update_status("❌ Şifre boş olamaz!", "red")
            messagebox.showwarning("Uyarı", "Lütfen şifre girin!")
            return
        
        if password != confirm:
            self.update_status("❌ Şifreler eşleşmiyor!", "red")
            messagebox.showerror("Hata", "Şifreler eşleşmiyor!")
            return
        
        self.operation_in_progress = True
        self.seal_btn.config(state=tk.DISABLED)
        self.unseal_btn.config(state=tk.DISABLED)
        self.destruct_btn.config(state=tk.DISABLED)
        
        self._stop_jammer()
        
        thread = threading.Thread(
            target=self._do_seal,
            args=(password,),
            daemon=True
        )
        thread.start()
    
    def _do_seal(self, password: str):
        """Arka planda mühürleme"""
        try:
            success = self.bastion.seal(self.selected_file, password)
            
            if success:
                self.root.after(0, lambda: self.update_status(
                    "✅ Mühürleme başarılı!", "green"
                ))
                self.root.after(0, lambda: self.clear_file())
                self.root.after(0, lambda: self.password_var.set(""))
                self.root.after(0, lambda: self.confirm_var.set(""))
                self.root.after(0, lambda: messagebox.showinfo(
                    "Başarılı", 
                    "Dosya başarıyla mühürlendi!"
                ))
            else:
                self.root.after(0, lambda: self.update_status(
                    "❌ Mühürleme başarısız!", "red"
                ))
                
        except Exception as e:
            self.root.after(0, lambda: self.update_status(
                f"❌ Hata: {str(e)}", "red"
            ))
            self.root.after(0, lambda: messagebox.showerror("Hata", str(e)))
            
        finally:
            # UI'ı aç
            self.root.after(0, lambda: self._unlock_ui())
            self.root.after(0, lambda: self._start_jammer())
    
    def unseal_file(self):
        """Kurtarma işlemi"""
        if self.operation_in_progress:
            self.update_status("⚠ İşlem zaten devam ediyor!", "yellow")
            return
        
        password = self.password_entry.get()
        
        if not password:
            self.update_status("❌ Şifre gerekli!", "red")
            messagebox.showwarning("Uyarı", "Lütfen şifre girin!")
            return
        
        
        self.operation_in_progress = True
        self.seal_btn.config(state=tk.DISABLED)
        self.unseal_btn.config(state=tk.DISABLED)
        self.destruct_btn.config(state=tk.DISABLED)
        
        self._stop_jammer()
        
        thread = threading.Thread(
            target=self._do_unseal,
            args=(password,),
            daemon=True
        )
        thread.start()
    
    def _do_unseal(self, password: str):
        """Arka planda kurtarma"""
        try:
            result = self.bastion.unseal(password)
            
            if result:
                self.root.after(0, lambda: self.update_status(
                    f"✅ Kurtarma başarılı: {os.path.basename(result)}", "green"
                ))
                self.root.after(0, lambda: self.password_var.set(""))
                self.root.after(0, lambda: messagebox.showinfo(
                    "Başarılı", 
                    f"Dosya kurtarıldı:\n{result}"
                ))
            else:
                self.root.after(0, lambda: self.update_status(
                    "❌ Kurtarma başarısız!", "red"
                ))
                
        except Exception as e:
            self.root.after(0, lambda: self.update_status(
                f"❌ Hata: {str(e)}", "red"
            ))
            self.root.after(0, lambda: messagebox.showerror("Hata", str(e)))
            
        finally:
            self.root.after(0, lambda: self._unlock_ui())
            self.root.after(0, lambda: self._start_jammer())
    
    def _unlock_ui(self):
        """UI'ı tekrar aktif et"""
        self.operation_in_progress = False
        self.seal_btn.config(state=tk.NORMAL)
        self.unseal_btn.config(state=tk.NORMAL)
        self.destruct_btn.config(state=tk.NORMAL)
    
    def backup_shares(self):
        """Shamir parçalarını yedekle"""
        backup_dir = filedialog.askdirectory(
            title="Yedekleme dizini seçin"
        )
        
        if backup_dir:
            thread = threading.Thread(
                target=self.bastion.backup_shares,
                args=(backup_dir,),
                daemon=True
            )
            thread.start()
    
    def restore_shares(self):
        """Shamir parçalarını geri yükle"""
        backup_dir = filedialog.askdirectory(
            title="Yedek dizinini seçin"
        )
        
        if backup_dir:
            thread = threading.Thread(
                target=self.bastion.restore_shares,
                args=(backup_dir,),
                daemon=True
            )
            thread.start()
    
    def self_destruct(self):
        """Kendini imha"""
        if messagebox.askyesno(
            "TEHLİKELİ İŞLEM!",
            "Tüm veriler silinecek!\n\nBu işlem geri alınamaz!\n\nDevam etmek istediğinize emin misiniz?",
            icon='warning'
        ):
            self.update_status("💥 SELF-DESTRUCT ACTIVATED!", "red")
            
            self.seal_btn.config(state=tk.DISABLED)
            self.unseal_btn.config(state=tk.DISABLED)
            self.destruct_btn.config(state=tk.DISABLED)
            
            thread = threading.Thread(
                target=self._do_self_destruct,
                daemon=True
            )
            thread.start()
    
    def _do_self_destruct(self):
        """Arka planda imha"""
        try:
            self.bastion.self_destruct()
            self.root.after(2000, lambda: self.root.quit())
        except Exception as e:
            self.root.after(0, lambda: self.update_status(f"❌ Hata: {e}", "red"))
    
    def _on_closing(self):
        """Uygulama kapanırken"""
        if self.operation_in_progress:
            messagebox.showwarning("Uyarı", "İşlem devam ederken çıkılamaz!")
            return
        
        if messagebox.askokcancel("Çıkış", "Uygulamadan çıkmak istediğinize emin misiniz?"):
            self._stop_jammer()
            self.root.destroy()


    def _check_developer_auth(self, event=None):
        """[ DEV-AUTH ] - Artık senin 'log' fonksiyonunu kullanıyor"""
        import socket
        import hashlib
        from datetime import datetime
        from tkinter import messagebox

        try:
            expected_sig = "9552140d7c2a5f11103c8005391694f2"
            current_arch = "THEVAL3X" 
            is_original = (hashlib.md5(current_arch.encode()).hexdigest() == expected_sig)

            host = socket.gethostname()
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            status = "VERIFIED ORIGINAL" if is_original else "CRACKED / MODIFIED"
            
            if is_original:
                self.log(f"[*] Core Identity Verified: {current_arch}", "info")
            else:
                self.log(f"[!] SECURITY BREACH: Unauthorized identity '{current_arch}'", "error")

            auth_info = (
                f"--- LEVIATHAN CORE ---\n\n"
                f"ARCHITECT: {current_arch}\n"
                f"NODE: {host}\n"
                f"TIME: {now}\n"
                f"STATUS: {status}"
            )

            if is_original:
                messagebox.showinfo("AUTH VERIFIED", auth_info)
            else:
                messagebox.showerror("SECURITY BREACH", auth_info)

        except Exception as e:
            print(f"Auth Error: {e}")



    def change_theme(self, theme_name):
        """Temayı değiştir - TÜM widget'lar güncellenir"""
        global GUI_COLORS, CURRENT_THEME
        
        if theme_name in THEMES:
            old_theme = CURRENT_THEME
            
            CURRENT_THEME = theme_name
            GUI_COLORS = THEMES[theme_name]
            
            try:
                self.root.configure(bg=GUI_COLORS['bg'])
                
                style = ttk.Style(self.root)
                style.theme_use('clam')
                style.configure(
                    "green.Horizontal.TProgressbar",
                    background=GUI_COLORS['success'],
                    troughcolor='#333333',
                    bordercolor=GUI_COLORS['success'],
                    lightcolor=GUI_COLORS['success'],
                    darkcolor=GUI_COLORS['success']
                )
                
                self._rebuild_ui()
                
                self.update_status(f"🎨 Tema değiştirildi: {THEMES[theme_name]['name']}", "green")
                self.log(f"✨ Yeni tema: {THEMES[theme_name]['name']}", "success")
                
                if hasattr(self, 'theme_indicator'):
                    self.theme_indicator.config(
                        text=f"✓ Aktif: {THEMES[theme_name]['name']}",
                        fg=GUI_COLORS['success']
                    )
                
            except Exception as e:
                CURRENT_THEME = old_theme
                GUI_COLORS = THEMES[old_theme]
                self.update_status(f"❌ Tema değiştirilemedi: {str(e)}", "red")
                self.log(f"Tema hatası: {str(e)}", "error")

    def _rebuild_ui(self):
        """UI'ı yeniden oluştur - Tema değişince çağrılır"""
        try:
            loading_frame = None
            if hasattr(self, 'loading_frame') and self.loading_frame:
                loading_frame = self.loading_frame
                self.loading_frame = None
            
            for widget in self.root.winfo_children():
                if widget != loading_frame: 
                    widget.destroy()
            
            self._setup_fonts()
            self._setup_ui()
            self._setup_hotkeys()
            
            if loading_frame:
                self.loading_frame = loading_frame
                self.loading_frame.lift()
            
            self.log(f"🔄 UI yeniden oluşturuldu (Tema: {THEMES[CURRENT_THEME]['name']})", "info")
            
        except Exception as e:
            print(f"UI rebuild hatası: {e}")
            self.root.after(1000, lambda: self.update_status("⚠ UI hatası, yeniden başlatın", "warning"))

    def _apply_theme(self):
        """Temayı tüm widget'lara uygula"""
        self.root.configure(bg=GUI_COLORS['bg'])
        
        style = ttk.Style(self.root)
        style.theme_use('clam')
        style.configure(
            "green.Horizontal.TProgressbar",
            background=GUI_COLORS['success'],
            troughcolor='#333333',
            bordercolor=GUI_COLORS['success']
        )
        
        self.log(f"Tema uygulandı: {THEMES[CURRENT_THEME]['name']}", "info")
    
    
    def run(self):
        """Uygulamayı başlat"""
        self.root.mainloop()



def main():
    """Ana program girişi"""
    try:
        
        print(f"{Colors.CYAN}")
        print("╔═══════════════════════════════════════════════════════════════╗")
        print("║  LEVIATHAN V1.0 - THE SINGULARITY BASTION                     ║")
        print("║  DEVELOPER: Valex                                             ║")
        print("║  STATUS: INITIALIZING...                                      ║")
        print("╚═══════════════════════════════════════════════════════════════╝")
        print(f"{Colors.END}")
        
        
        print(f"{Colors.BLUE}[*] Initializing Obsidian Bastion...{Colors.END}")
        
        
        bastion = ObsidianBastion()
        
        print(f"{Colors.GREEN}[✓] Bastion initialized successfully{Colors.END}")
        print(f"{Colors.GRAY}    Vault: {bastion.vault_root}{Colors.END}")
        print(f"{Colors.GRAY}    HWID: {bastion.hwid.hex()[:32]}...{Colors.END}")
        
        
        print(f"{Colors.BLUE}[*] Starting GUI...{Colors.END}")
        app = LeviathanGUI(bastion)
        
        print(f"{Colors.GREEN}[✓] GUI started successfully{Colors.END}")
        print(f"{Colors.YELLOW}[!] Press Ctrl+Q to exit{Colors.END}\n")
        
        
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[!] Interrupted by user{Colors.END}")
        sys.exit(0)
        
    except Exception as e:
        print(f"{Colors.RED}[!] Fatal error: {e}{Colors.END}")
        traceback.print_exc()
        input("\nPress Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()
