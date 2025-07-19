/* EmailWidget Documentation Custom JavaScript */

document.addEventListener('DOMContentLoaded', function() {
    // 确保表格在文档加载后正确渲染
    function fixTableWidths() {
        // 修复所有表格的宽度问题
        const tables = document.querySelectorAll('.md-content table');
        tables.forEach(table => {
            // 强制设置表格宽度
            table.style.setProperty('width', '100%', 'important');
            table.style.setProperty('max-width', '100%', 'important');
            table.style.setProperty('table-layout', 'auto', 'important');
            table.style.setProperty('border-collapse', 'collapse', 'important');
            table.style.setProperty('margin', '0', 'important');
            
            // 修复表格父容器
            if (table.parentElement) {
                table.parentElement.style.setProperty('width', '100%', 'important');
                table.parentElement.style.setProperty('max-width', '100%', 'important');
                table.parentElement.style.setProperty('overflow', 'visible', 'important');
            }
            
            // 修复表格单元格
            const cells = table.querySelectorAll('th, td');
            cells.forEach(cell => {
                cell.style.wordWrap = 'break-word';
                cell.style.overflow = 'hidden';
            });
        });
        
        // 特别修复文档中的演示表格
        const demoTables = document.querySelectorAll('div[style*="padding: 16px"] table');
        demoTables.forEach(table => {
            table.style.setProperty('width', '100%', 'important');
            table.style.setProperty('max-width', '100%', 'important');
            table.style.setProperty('border-collapse', 'collapse', 'important');
        });
        
        // 修复组件预览中的表格
        const previewTables = document.querySelectorAll('.component-preview table');
        previewTables.forEach(table => {
            table.style.setProperty('width', '100%', 'important');
            table.style.setProperty('max-width', '100%', 'important');
            table.style.setProperty('margin', '0', 'important');
        });
        
        // 移除可能的响应式包装器限制
        const scrollWraps = document.querySelectorAll('.md-typeset__scrollwrap');
        scrollWraps.forEach(wrap => {
            wrap.style.setProperty('width', '100%', 'important');
            wrap.style.setProperty('max-width', '100%', 'important');
            wrap.style.setProperty('overflow', 'visible', 'important');
        });
    }
    
    // 立即执行修复
    fixTableWidths();
    
    // 监听可能的动态内容加载
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.addedNodes.length > 0) {
                // 检查是否有新的表格添加
                const hasNewTables = Array.from(mutation.addedNodes).some(node => {
                    return node.nodeType === 1 && (
                        node.tagName === 'TABLE' || 
                        node.querySelector && node.querySelector('table')
                    );
                });
                
                if (hasNewTables) {
                    // 延迟执行以确保 DOM 完全更新
                    setTimeout(fixTableWidths, 100);
                }
            }
        });
    });
    
    // 观察文档内容区域的变化
    const contentArea = document.querySelector('.md-content');
    if (contentArea) {
        observer.observe(contentArea, {
            childList: true,
            subtree: true
        });
    }
    
    // 当窗口大小改变时重新修复表格
    window.addEventListener('resize', function() {
        setTimeout(fixTableWidths, 100);
    });
    
    // 修复可能的懒加载内容
    if ('IntersectionObserver' in window) {
        const lazyObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const target = entry.target;
                    const tables = target.querySelectorAll('table');
                    if (tables.length > 0) {
                        setTimeout(fixTableWidths, 50);
                    }
                }
            });
        });
        
        // 观察所有可能包含表格的容器
        const containers = document.querySelectorAll('.component-preview, .md-typeset');
        containers.forEach(container => {
            lazyObserver.observe(container);
        });
    }
});

// 为 Material 主题的特殊处理
if (typeof window !== 'undefined' && window.addEventListener) {
    window.addEventListener('load', function() {
        // 确保在所有资源加载完成后再次修复表格
        setTimeout(function() {
            const tables = document.querySelectorAll('.md-content table');
            tables.forEach(table => {
                table.style.width = '100%';
                table.style.maxWidth = '100%';
                
                // 移除可能的宽度限制类
                table.classList.remove('narrow');
                if (table.parentElement) {
                    table.parentElement.style.overflow = 'visible';
                }
            });
        }, 500);
    });
}