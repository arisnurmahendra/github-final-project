// Enhanced Shipping Calculator JavaScript
class ShippingCalculator {
    constructor() {
        this.rates = {
            standard: { rate: 2.50, base: 5.00, days: 5 },
            express: { rate: 4.00, base: 12.00, days: 2 },
            overnight: { rate: 7.50, base: 25.00, days: 1 }
        };
        
        this.init();
    }
    
    init() {
        const form = document.getElementById('shippingForm');
        const useZipCheckbox = document.getElementById('useZip');
        const zipFields = document.getElementById('zipFields');
        
        // Toggle ZIP code fields
        useZipCheckbox.addEventListener('change', () => {
            zipFields.classList.toggle('hidden', !useZipCheckbox.checked);
        });
        
        // Handle form submission
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.calculateShipping();
        });
    }
    
    validateZipCode(zip) {
        const zipPattern = /^\d{5}(-\d{4})?$/;
        return zipPattern.test(zip.trim());
    }
    
    calculateDistanceMultiplier(originZip, destZip) {
        const origin = parseInt(originZip.substring(0, 5));
        const dest = parseInt(destZip.substring(0, 5));
        const diff = Math.abs(origin - dest);
        
        if (diff < 10000) return 1.0;      // Local
        if (diff < 30000) return 1.3;      // Regional
        if (diff < 50000) return 1.6;      // National
        return 2.0;                        // Cross-country
    }
    
    calculateShipping() {
        try {
            // Get form values
            const weight = parseFloat(document.getElementById('weight').value);
            const service = document.getElementById('service').value;
            const useZip = document.getElementById('useZip').checked;
            
            // Validate inputs
            if (!weight || weight <= 0 || weight > 50) {
                throw new Error('Weight must be between 0.1 and 50 kg');
            }
            
            if (!service) {
                throw new Error('Please select a service type');
            }
            
            let originZip = '';
            let destZip = '';
            let distanceMultiplier = 1.0;
            
            if (useZip) {
                originZip = document.getElementById('originZip').value.trim();
                destZip = document.getElementById('destZip').value.trim();
                
                if (!originZip || !destZip) {
                    throw new Error('Please enter both ZIP codes');
                }
                
                if (!this.validateZipCode(originZip) || !this.validateZipCode(destZip)) {
                    throw new Error('Please enter valid ZIP codes (12345 or 12345-6789)');
                }
                
                distanceMultiplier = this.calculateDistanceMultiplier(originZip, destZip);
            }
            
            // Calculate costs
            const serviceData = this.rates[service];
            const baseCost = serviceData.base;
            const weightCost = weight * serviceData.rate;
            const subtotal = baseCost + weightCost;
            let totalCost = subtotal * distanceMultiplier;
            
            // Apply volume discount
            const discountApplied = weight > 20;
            if (discountApplied) {
                totalCost *= 0.9; // 10% discount
            }
            
            // Calculate delivery date
            const deliveryDate = this.calculateDeliveryDate(serviceData.days);
            
            const result = {
                service,
                weight,
                baseCost,
                weightCost,
                subtotal,
                distanceMultiplier,
                totalCost,
                deliveryDays: serviceData.days,
                deliveryDate,
                discountApplied,
                useZip,
                originZip,
                destZip
            };
            
            this.displayResults(result);
            this.showComparison(weight, distanceMultiplier, useZip, originZip, destZip);
            
        } catch (error) {
            alert(`Error: ${error.message}`);
        }
    }
    
    calculateDeliveryDate(days) {
        const date = new Date();
        let businessDays = 0;
        
        while (businessDays < days) {
            date.setDate(date.getDate() + 1);
            // Skip weekends
            if (date.getDay() !== 0 && date.getDay() !== 6) {
                businessDays++;
            }
        }
        
        return date.toLocaleDateString();
    }
    
    displayResults(result) {
        const resultsDiv = document.getElementById('results');
        const quoteDetails = document.getElementById('quoteDetails');
        
        let distanceInfo = '';
        if (result.useZip) {
            const distanceType = this.getDistanceType(result.distanceMultiplier);
            distanceInfo = `
                <div class="detail-row">
                    <span>Distance (${result.originZip} → ${result.destZip}):</span>
                    <span>${distanceType} (${result.distanceMultiplier}x)</span>
                </div>
            `;
        }
        
        let discountInfo = '';
        if (result.discountApplied) {
            discountInfo = '<span class="discount-badge">Volume Discount Applied</span>';
        }
        
        quoteDetails.innerHTML = `
            <div class="detail-row">
                <span>Service Type:</span>
                <span>${result.service.charAt(0).toUpperCase() + result.service.slice(1)}</span>
            </div>
            <div class="detail-row">
                <span>Package Weight:</span>
                <span>${result.weight} kg</span>
            </div>
            <div class="detail-row">
                <span>Base Cost:</span>
                <span>$${result.baseCost.toFixed(2)}</span>
            </div>
            <div class="detail-row">
                <span>Weight Cost:</span>
                <span>$${result.weightCost.toFixed(2)}</span>
            </div>
            ${distanceInfo}
            <div class="detail-row total">
                <span>Total Cost:${discountInfo}</span>
                <span>$${result.totalCost.toFixed(2)}</span>
            </div>
            <div class="detail-row">
                <span>Estimated Delivery:</span>
                <span>${result.deliveryDays} business days (${result.deliveryDate})</span>
            </div>
        `;
        
        resultsDiv.classList.remove('hidden');
    }
    
    getDistanceType(multiplier) {
        if (multiplier === 1.0) return 'Local';
        if (multiplier === 1.3) return 'Regional';
        if (multiplier === 1.6) return 'National';
        return 'Cross-country';
    }
    
    showComparison(weight, distanceMultiplier, useZip, originZip, destZip) {
        const comparisonDiv = document.getElementById('comparison');
        const comparisonTable = document.getElementById('comparisonTable');
        
        let html = '<div class="comparison-grid">';
        
        Object.entries(this.rates).forEach(([service, data]) => {
            const baseCost = data.base;
            const weightCost = weight * data.rate;
            const subtotal = baseCost + weightCost;
            let totalCost = subtotal * distanceMultiplier;
            
            // Apply volume discount
            if (weight > 20) {
                totalCost *= 0.9;
            }
            
            html += `
                <div class="comparison-item">
                    <div>
                        <div class="service-name">${service.charAt(0).toUpperCase() + service.slice(1)}</div>
                        <div class="service-time">${data.days} business days</div>
                    </div>
                    <div class="service-price">$${totalCost.toFixed(2)}</div>
                </div>
            `;
        });
        
        html += '</div>';
        comparisonTable.innerHTML = html;
        comparisonDiv.classList.remove('hidden');
    }
}

// Initialize calculator when page loads
document.addEventListener('DOMContentLoaded', () => {
    new ShippingCalculator();
});