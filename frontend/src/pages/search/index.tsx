import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import { Html5Qrcode } from 'html5-qrcode';

export default function SearchPage() {
  const [searchId, setSearchId] = useState('');
  const [isScanning, setIsScanning] = useState(true);
  const router = useRouter();

  const handleSearch = (id?: string) => {
    const idToSearch = id || searchId;
    if (idToSearch.trim()) {
      router.push(`/search/${idToSearch.trim()}`);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };

  useEffect(() => {
    if (!isScanning) return;
    
    let html5QrCode: Html5Qrcode | null = null;

    const startScanner = async () => {
      try {
        html5QrCode = new Html5Qrcode('qr-reader');
        
        const config = { 
          fps: 10, 
          qrbox: { width: 200, height: 200 }
        };
        
        await html5QrCode.start(
          { facingMode: "environment" },
          config,
          (decodedText, decodedResult) => {
            console.log('QR Code detected:', decodedText);
            setSearchId(decodedText);
            handleSearch(decodedText);
          },
          (errorMessage) => {} //continue scanning - ignore error
        );
        
        console.log('Scanner started successfully');
      } catch (err) {
        console.error('Unable to start scanner:', err);
      }
    };

    // Start scanner after small delay
    const timeout = setTimeout(startScanner, 100);

    return () => {
      clearTimeout(timeout);
      if (html5QrCode && html5QrCode.isScanning) {
        html5QrCode.stop().then(() => {
          console.log('Scanner stopped');
        }).catch((err) => {
          console.error('Error stopping scanner:', err);
        });
      }
    };
  }, [isScanning]);

  return (
    <div className="max-w-2xl mx-auto">
      <div className="bg-white rounded-2xl shadow-xl p-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-2">Search Medicine</h1>
        <p className="text-gray-600 mb-8">Find medicine by scanning QR code or entering ID manually</p>

        {/* QR Code Scanner Section */}
        <div className="mb-8">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-xl font-semibold text-gray-800">QR Code Scanner</h2>
            <button
              onClick={() => setIsScanning(!isScanning)}
              className={`
                px-6 py-3 rounded-lg font-semibold transition-all duration-300 transform hover:scale-105 cursor-pointer
                ${isScanning
                  ? 'bg-red-500 hover:bg-red-600 text-white shadow-lg'
                  : 'bg-blue-600 hover:bg-blue-700 text-white shadow-lg'
                }
              `}
            >
              {isScanning ? 'Close Scanner' : 'Open Scanner'}
            </button>
          </div>

          {/* QR Code Scanner */}
          {isScanning && (
            <div className="bg-gray-100 rounded-xl p-4 border-2 border-blue-300 shadow-inner">
              <div id="qr-reader" style={{ width: '100%' }}></div>
            </div>
          )}
          
          {!isScanning && (
            <div className="bg-gradient-to-br from-blue-50 to-blue-100 rounded-xl p-8 border-2 border-dashed border-blue-300">
              <div className="text-center text-gray-600">
                <p className="text-lg">Click "Open Scanner" to scan a QR code</p>
              </div>
            </div>
          )}
        </div>

        {/* Divider */}
        <div className="flex items-center gap-4 my-8">
          <div className="flex-1 h-px bg-gray-300"></div>
          <span className="text-gray-500 font-medium">OR</span>
          <div className="flex-1 h-px bg-gray-300"></div>
        </div>

        {/* Manual Search Section */}
        <div>
          <h2 className="text-xl font-semibold text-gray-800 mb-4">Manual Search</h2>
          <div className="space-y-4">
            <div>
              <input
                type="text"
                value={searchId}
                onChange={(e) => setSearchId(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="Enter 11-digit medicine ID (e.g., 10241126400)"
                maxLength={11}
                className="w-full px-4 py-3 border-2 border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all font-mono text-lg"
              />
              <p className="text-xs text-gray-500 mt-2">
                Press Enter to search
              </p>
            </div>

            <button
              onClick={() => handleSearch()}
              disabled={!searchId.trim()}
              className={`
                w-full px-6 py-4 rounded-lg font-semibold text-lg transition-all duration-300 transform cursor-pointer
                ${searchId.trim()
                  ? 'bg-gradient-to-r from-green-500 to-green-600 hover:from-green-600 hover:to-green-700 text-white shadow-lg hover:shadow-xl hover:scale-105'
                  : 'bg-gray-300 text-gray-500 cursor-not-allowed'
                }
              `}
            >
              Search Medicine
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
